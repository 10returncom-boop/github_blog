# -*- coding: utf-8 -*-
"""
全台建案統計儀表板 - HTML 生成器
生成：dashboard.html（總覽+縣市表+個案庫）+ counties/xxx.html（縣市子頁含區級表）
"""
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data")
COUNTIES_DIR = os.path.join(BASE, "counties")

# 讀取資料
with open(os.path.join(DATA_DIR, 'overview.json'), 'r', encoding='utf-8') as f:
    overview = json.load(f)
with open(os.path.join(DATA_DIR, 'county_stats.json'), 'r', encoding='utf-8') as f:
    county_stats = json.load(f)
with open(os.path.join(DATA_DIR, 'district_stats.json'), 'r', encoding='utf-8') as f:
    district_stats = json.load(f)
with open(os.path.join(DATA_DIR, 'case_db.json'), 'r', encoding='utf-8') as f:
    case_db = json.load(f)

# 縣市代碼對照
COUNTY_CODES = {
    '臺北市':'taipei','新北市':'newtaipei','桃園市':'taoyuan','臺中市':'taichung',
    '臺南市':'tainan','高雄市':'kaohsiung','嘉義市':'chiayi','彰化縣':'changhua',
    '基隆市':'keelung','新竹市':'hsinchu','新竹縣':'hsinchu_county','苗栗縣':'miaoli',
    '南投縣':'nantou','雲林縣':'yunlin','嘉義縣':'chiayi_county','屏東縣':'pingtung',
    '宜蘭縣':'yilan','花蓮縣':'hualien','臺東縣':'taitung','澎湖縣':'penghu',
    '金門縣':'kinmen','連江縣':'lienchiang','未標註':'unknown'
}

def county_slug(name):
    return COUNTY_CODES.get(name, name)

# 排序縣市：有資料的六都在前，有資料非六都次之，待補縣市最後
def county_sort_key(c):
    has_data = 0 if c.get('has_data', True) else 2
    capital = 0 if c['is_six_capital'] else 1
    return (has_data, capital, -c['total_buildings'])
county_stats_sorted = sorted(county_stats, key=county_sort_key)

# ========== 共用 CSS ==========
CSS = """
:root{
  --c-primary:#1a3a5c;--c-primary-light:#2d5a8a;--c-accent:#d4a017;
  --c-danger:#b8453a;--c-success:#2d6a4f;--c-info:#3a7ca5;
  --c-bg:#f5f3ef;--c-surface:#fff;--c-text:#2d2d2d;--c-text2:#6b6b6b;
  --c-border:#e0ddd6;--c-border-l:#eeebe4;
  --font-serif:'Noto Serif TC',serif;--font-sans:'Noto Sans TC',sans-serif;
  --radius:4px;--shadow-sm:0 1px 3px rgba(0,0,0,.06);--shadow-md:0 4px 12px rgba(0,0,0,.1);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-sans);background:var(--c-bg);color:var(--c-text);line-height:1.6;font-size:14px}
a{color:var(--c-primary);text-decoration:none}
a:hover{color:var(--c-accent)}
.header{background:var(--c-primary);color:#fff;padding:16px 24px;border-bottom:3px solid var(--c-accent)}
.header h1{font-family:var(--font-serif);font-size:22px;font-weight:700}
.header .sub{font-size:12px;opacity:.7;margin-top:2px}
.container{max-width:1400px;margin:0 auto;padding:20px 24px}
.tabs{display:flex;gap:0;border-bottom:2px solid var(--c-primary);margin-bottom:20px}
.tab{padding:10px 20px;cursor:pointer;font-size:14px;font-weight:600;color:var(--c-text2);border-bottom:3px solid transparent;margin-bottom:-2px;transition:all .2s}
.tab:hover{color:var(--c-primary)}
.tab.active{color:var(--c-primary);border-bottom-color:var(--c-accent)}
.tab-content{display:none}
.tab-content.active{display:block}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-bottom:24px}
.kpi-card{background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);padding:16px;position:relative;overflow:hidden}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--c-primary)}
.kpi-card.accent::before{background:var(--c-accent)}
.kpi-card.danger::before{background:var(--c-danger)}
.kpi-card.success::before{background:var(--c-success)}
.kpi-card.info::before{background:var(--c-info)}
.kpi-value{font-family:var(--font-serif);font-size:28px;font-weight:900;color:var(--c-primary);line-height:1.2}
.kpi-value.pending{color:#ccc;font-size:18px}
.kpi-label{font-size:12px;color:var(--c-text2);margin-top:6px}
.kpi-note{font-size:10px;color:#999;margin-top:3px}
.section{margin-bottom:32px}
.section-title{font-family:var(--font-serif);font-size:18px;font-weight:700;color:var(--c-primary);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--c-primary)}
.table-wrap{background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);overflow:hidden;overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:13px;min-width:600px}
th{background:var(--c-primary);color:#fff;padding:10px 12px;text-align:left;font-weight:600;font-size:12px;white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid var(--c-border-l)}
tr:last-child td{border-bottom:none}
tr:hover td{background:var(--c-bg)}
.num{text-align:right;font-variant-numeric:tabular-nums}
.center{text-align:center}
.badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600}
.badge.capital{background:var(--c-accent);color:var(--c-primary)}
.badge.non-capital{background:var(--c-bg);color:var(--c-text2)}
.badge.type{background:var(--c-bg-alt);color:var(--c-text2)}
.badge.redev{background:#e8f4fd;color:var(--c-info)}
.search-box{position:relative;margin-bottom:12px}
.search-box input{width:100%;padding:10px 14px 10px 36px;border:1px solid var(--c-border);border-radius:var(--radius);font-size:14px}
.search-box input:focus{outline:none;border-color:var(--c-primary)}
.search-icon{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:#999}
.filter-row{display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap}
.filter-row select{padding:8px 12px;border:1px solid var(--c-border);border-radius:var(--radius);font-size:13px}
.result-info{font-size:13px;color:var(--c-text2);margin-bottom:8px}
.result-info strong{color:var(--c-primary)}
.pagination{display:flex;justify-content:center;gap:6px;margin-top:16px;flex-wrap:wrap}
.page-btn{padding:6px 12px;border:1px solid var(--c-border);border-radius:var(--radius);font-size:13px;cursor:pointer;background:var(--c-surface)}
.page-btn:hover{border-color:var(--c-primary);color:var(--c-primary)}
.page-btn.active{background:var(--c-primary);color:#fff;border-color:var(--c-primary)}
.page-btn:disabled{opacity:.4;cursor:not-allowed}
.chart-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:24px}
.chart-card{background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);padding:16px}
.chart-title{font-family:var(--font-serif);font-size:14px;font-weight:700;color:var(--c-primary);margin-bottom:4px}
.chart-sub{font-size:11px;color:var(--c-text2);margin-bottom:12px}
.chart-container{width:100%;min-height:280px}
.breadcrumb{font-size:13px;color:var(--c-text2);margin-bottom:16px}
.breadcrumb a{color:var(--c-primary)}
.breadcrumb .sep{margin:0 6px;color:#999}
.footer{background:var(--c-primary);color:rgba(255,255,255,.6);padding:20px;text-align:center;font-size:12px;margin-top:40px}
.footer strong{color:var(--c-accent)}
.pending-note{background:#fff8e1;border:1px solid #ffe082;border-radius:var(--radius);padding:12px 16px;margin-bottom:16px;font-size:13px;color:#795548}
.pending-note strong{color:#e65100}
@media(max-width:768px){.chart-grid{grid-template-columns:1fr}.kpi-grid{grid-template-columns:repeat(2,1fr)}.container{padding:12px}}
"""

# ========== 共用 JS ==========
def make_js(data_name, data_json):
    return f"""
<script>
const {data_name} = {data_json};
</script>
"""

# ========== 主頁面 dashboard.html ==========
print("=== 生成主頁面 dashboard.html ===")

# 準備圖表資料（僅有資料的縣市）
county_chart_data = json.dumps([
    {'name': c['county'], 'value': c['total_buildings'], 'hh': c['total_households'], 'capital': c['is_six_capital']}
    for c in county_stats_sorted if c.get('has_data', True)
], ensure_ascii=False)

building_type_data = json.dumps(
    {t: sum(c['building_types'].get(t,0) for c in county_stats) for t in ['大樓','華廈','社區','公寓','其他']},
    ensure_ascii=False
)

index_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全台建案統計儀表板 | 不動產資料彙整平台</title>
<link rel="stylesheet" href="https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.6.0/dist/echarts.min.js" integrity="sha384-pPi0zxBAoDu6+JXW/C68UZLvBUUtU+7zonhif43rqj7pxsGyqyqzcian2Rj37Rss" crossorigin="anonymous"></script>
<style>{CSS}</style>
</head>
<body>

<div class="header">
  <h1>全台建案統計儀表板</h1>
  <div class="sub">不動產資料彙整平台 · 版本 {overview['version']} · 更新 {overview['timestamp']}</div>
</div>

<div class="container">

  <!-- 資料狀態提示 -->
  <div class="pending-note">
    <strong>資料狀態（22縣市）：</strong>已彙整 <strong>{overview['counties_with_data']} 縣市</strong>（{overview['total_buildings']:,} 筆公寓大廈報備資料），
    另有 <strong>{overview['counties_pending']} 縣市</strong>（基隆市、新竹縣、苗栗縣、南投縣、雲林縣、嘉義縣、高雄市、屏東縣、宜蘭縣、花蓮縣、臺東縣、澎湖縣、金門縣、連江縣）之公寓大廈報備開放資料尚未釋出，標示為「待補」。
    <strong>建照/使照/待售/預售</strong>等指標亦待匯入開放資料。
  </div>

  <!-- Tabs -->
  <div class="tabs">
    <div class="tab active" data-tab="overview">總覽指標</div>
    <div class="tab" data-tab="county">縣市別主表</div>
    <div class="tab" data-tab="cases">個案建案明細庫</div>
  </div>

  <!-- Tab 1: 總覽指標 -->
  <div class="tab-content active" id="tab-overview">
    <div class="section">
      <div class="section-title">全台總覽指標</div>
      <div class="kpi-grid">
        <div class="kpi-card"><div class="kpi-value">{overview['total_counties']}</div><div class="kpi-label">全台縣市總數</div><div class="kpi-note">六都6 + 非六都16</div></div>
        <div class="kpi-card success"><div class="kpi-value">{overview['counties_with_data']}</div><div class="kpi-label">已彙整縣市</div><div class="kpi-note">{overview['counties_with_data']/overview['total_counties']*100:.0f}% 覆蓋率</div></div>
        <div class="kpi-card danger"><div class="kpi-value">{overview['counties_pending']}</div><div class="kpi-label">待補開放資料縣市</div><div class="kpi-note">尚未釋出公寓大廈報備資料</div></div>
        <div class="kpi-card"><div class="kpi-value">{overview['total_buildings']:,}</div><div class="kpi-label">公寓大廈報備總棟數</div><div class="kpi-note">{overview['counties_with_data']} 縣市 / {overview['total_districts']} 區</div></div>
        <div class="kpi-card accent"><div class="kpi-value">{overview['total_households']:,}</div><div class="kpi-label">報備總戶數</div><div class="kpi-note">僅臺中/嘉義有戶數資料</div></div>
        <div class="kpi-card info"><div class="kpi-value">{overview['redev_count']:,}</div><div class="kpi-label">標註重劃區建案</div><div class="kpi-note">依名稱/地址關鍵字比對</div></div>
        <div class="kpi-card success"><div class="kpi-value">{overview['buildings_with_addr']:,}</div><div class="kpi-label">有完整住址</div><div class="kpi-note">{overview['buildings_with_addr']/overview['total_buildings']*100:.1f}% 覆蓋率</div></div>
      </div>
    </div>

    <div class="section">
      <div class="section-title">建照 / 使用執照 / 待售 / 預售（待補開放資料）</div>
      <div class="kpi-grid">
        <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">全台建照年度累計件數</div><div class="kpi-note">含核發戶數、總棟數、樓地板面積</div></div>
        <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">全台使用執照年度累計件數</div><div class="kpi-note">含完工件數、完工戶數、總棟數</div></div>
        <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">待售新成屋總宅數</div><div class="kpi-note">來源：內政部不動產資訊平台</div></div>
        <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">預售屋建案總件數</div><div class="kpi-note">來源：實價登錄開放CSV聚合</div></div>
      </div>
    </div>

    <div class="section">
      <div class="section-title">視覺化分析</div>
      <div class="chart-grid">
        <div class="chart-card"><div class="chart-title">各縣市建案數量</div><div class="chart-sub">公寓大廈報備棟數排名（六都標註）</div><div class="chart-container" id="chart-county"></div></div>
        <div class="chart-card"><div class="chart-title">建物型態分布</div><div class="chart-sub">大樓 / 華廈 / 社區 / 公寓 / 其他</div><div class="chart-container" id="chart-btype"></div></div>
      </div>
    </div>
  </div>

  <!-- Tab 2: 縣市別主表 -->
  <div class="tab-content" id="tab-county">
    <div class="section">
      <div class="section-title">縣市別主表（點擊縣市進入區級子表與個案）</div>
      <div class="table-wrap">
        <table>
          <thead><tr>
            <th>縣市</th><th class="center">六都</th>
            <th class="num">報備建案數</th><th class="num">報備戶數</th>
            <th class="num">行政區數</th><th class="num">重劃區標註</th>
            <th class="num">建照件數</th><th class="num">建照戶數</th>
            <th class="num">使照件數</th><th class="num">使照戶數</th>
            <th class="num">第一次登記棟數</th>
            <th class="num">待售新成屋宅數</th>
            <th class="num">預售屋件數</th><th class="num">預售戶數</th>
            <th>操作</th>
          </tr></thead>
          <tbody>
"""

for c in county_stats_sorted:
    slug = county_slug(c['county'])
    capital_badge = '<span class="badge capital">六都</span>' if c['is_six_capital'] else '<span class="badge non-capital">非六都</span>'
    has_data = c.get('has_data', True)
    if has_data:
        index_html += f"""            <tr>
              <td><strong><a href="counties/{slug}.html">{c['county']}</a></strong></td>
              <td class="center">{capital_badge}</td>
              <td class="num">{c['total_buildings']:,}</td>
              <td class="num">{c['total_households']:,}</td>
              <td class="num">{c['district_count']}</td>
              <td class="num">{c['redev_zone_count']}</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td class="num" style="color:#ccc">待補</td>
              <td><a href="counties/{slug}.html" class="page-btn" style="padding:3px 10px;font-size:12px">進入 &rarr;</a></td>
            </tr>
"""
    else:
        index_html += f"""            <tr style="background:#fafafa;color:#999">
              <td><strong style="color:#999">{c['county']}</strong> <span class="badge" style="background:#eee;color:#999">待補</span></td>
              <td class="center">{capital_badge}</td>
              <td class="num" colspan="5" style="color:#bbb">— 開放資料尚未釋出 —</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td class="num" style="color:#ddd">待補</td>
              <td style="color:#ccc">—</td>
            </tr>
"""

index_html += f"""          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- Tab 3: 個案建案明細庫 -->
  <div class="tab-content" id="tab-cases">
    <div class="section">
      <div class="section-title">個案建案明細庫（{overview['total_buildings']:,} 筆）</div>
      <div class="search-box"><span class="search-icon">&#128269;</span><input type="text" id="case-search" placeholder="搜尋建案名稱、地址、使照序號..."></div>
      <div class="filter-row">
        <select id="filter-county"><option value="">全部縣市</option></select>
        <select id="filter-district"><option value="">全部行政區</option></select>
        <select id="filter-type"><option value="">全部建物型態</option><option>大樓</option><option>華廈</option><option>社區</option><option>公寓</option><option>其他</option></select>
        <select id="filter-redev"><option value="">全部</option><option value="1">有重劃區標註</option></select>
      </div>
      <div class="result-info" id="case-result"></div>
      <div class="table-wrap">
        <table id="case-table">
          <thead><tr>
            <th>使照序號</th><th>建案名稱</th><th>縣市</th><th>行政區</th>
            <th>地址</th><th class="num">戶數</th><th>建物型態</th><th>管理組織</th><th>重劃區</th>
          </tr></thead>
          <tbody id="case-tbody"></tbody>
        </table>
      </div>
      <div class="pagination" id="case-pagination"></div>
    </div>
  </div>

</div>

<div class="footer">
  <p><strong>全台建案統計儀表板</strong> · 資料來源：各縣市政府公寓大廈報備開放資料 · 版本 {overview['version']} · 更新 {overview['timestamp']}</p>
  <p>建照/使照/待售/預售指標待匯入開放資料 · 本平台僅供研究參考</p>
</div>

{make_js('COUNTY_DATA', county_chart_data)}
{make_js('BTYPE_DATA', building_type_data)}
{make_js('CASE_DB', json.dumps(case_db, ensure_ascii=False))}

<script>
// Tab 切換
document.querySelectorAll('.tab').forEach(t=>{{
  t.addEventListener('click',()=>{{
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    document.getElementById('tab-'+t.dataset.tab).classList.add('active');
    if(t.dataset.tab==='overview'){{renderCharts()}}
  }});
}});

// 圖表
let chartsRendered=false;
function renderCharts(){{
  if(chartsRendered)return;chartsRendered=true;
  const c1=echarts.init(document.getElementById('chart-county'));
  c1.setOption({{
    tooltip:{{trigger:'axis',axisPointer:{{type:'shadow'}}}},
    grid:{{left:'3%',right:'5%',bottom:'15%',containLabel:true}},
    xAxis:{{type:'category',data:COUNTY_DATA.map(d=>d.name),axisLabel:{{rotate:30,fontSize:11}}}},
    yAxis:{{type:'value',name:'建案數'}},
    series:[{{type:'bar',data:COUNTY_DATA.map(d=>({{value:d.value,itemStyle:{{color:d.capital?'#d4a017':'#1a3a5c'}}}})),barMaxWidth:40,label:{{show:true,position:'top',fontSize:10}}}}]
  }});
  new ResizeObserver(()=>c1.resize()).observe(document.getElementById('chart-county'));
  const c2=echarts.init(document.getElementById('chart-btype'));
  const bd=Object.entries(BTYPE_DATA);
  c2.setOption({{
    tooltip:{{trigger:'item',formatter:'{{b}}: {{c}} 棟 ({{d}}%)'}},
    legend:{{bottom:0}},
    series:[{{type:'pie',radius:['40%','70%'],center:['50%','45%'],
      data:bd.map(([k,v])=>({{name:k,value:v}})),
      label:{{formatter:'{{b}}\\n{{d}}%',fontSize:11}},itemStyle:{{borderColor:'#fff',borderWidth:2}}
    }}],color:['#1a3a5c','#d4a017','#2d6a4f','#b8453a','#999']
  }});
  new ResizeObserver(()=>c2.resize()).observe(document.getElementById('chart-btype'));
}}
setTimeout(renderCharts,300);

// 個案庫搜尋篩選分頁
const PER_PAGE=50;let page=1,filtered=[];
const tbody=document.getElementById('case-tbody');
const resultEl=document.getElementById('case-result');
const pagEl=document.getElementById('case-pagination');

// 載入篩選選項
const counties=[...new Set(CASE_DB.map(b=>b.county))].sort();
const fc=document.getElementById('filter-county');
counties.forEach(c=>{{const o=document.createElement('option');o.value=c;o.textContent=c;fc.appendChild(o)}});
fc.addEventListener('change',()=>{{
  const fd=document.getElementById('filter-district');
  fd.innerHTML='<option value="">全部行政區</option>';
  const dists=[...new Set(CASE_DB.filter(b=>b.county===fc.value).map(b=>b.district))].sort();
  dists.forEach(d=>{{const o=document.createElement('option');o.value=d;o.textContent=d;fd.appendChild(o)}});
  applyFilter();
}});
['filter-district','filter-type','filter-redev','case-search'].forEach(id=>{{
  document.getElementById(id).addEventListener('input',applyFilter);
  document.getElementById(id).addEventListener('change',applyFilter);
}});

function applyFilter(){{
  const q=document.getElementById('case-search').value.trim().toLowerCase();
  const c=document.getElementById('filter-county').value;
  const d=document.getElementById('filter-district').value;
  const t=document.getElementById('filter-type').value;
  const r=document.getElementById('filter-redev').value;
  filtered=CASE_DB.filter(b=>{{
    if(q&&!(b.name.toLowerCase().includes(q)||b.address.toLowerCase().includes(q)||b.id.toLowerCase().includes(q)))return false;
    if(c&&b.county!==c)return false;
    if(d&&b.district!==d)return false;
    if(t&&b.building_type!==t)return false;
    if(r==='1'&&!b.redev_zone)return false;
    return true;
  }});
  page=1;renderCases();
}}

function renderCases(){{
  resultEl.innerHTML='共 <strong>'+filtered.length.toLocaleString()+'</strong> 筆結果';
  const start=(page-1)*PER_PAGE;
  const pageData=filtered.slice(start,start+PER_PAGE);
  tbody.innerHTML=pageData.map(b=>{{
    const rt=b.redev_zone?'<span class="badge redev">'+b.redev_zone+'</span>':'';
    return '<tr><td>'+b.id+'</td><td><strong>'+b.name+'</strong></td><td>'+b.county+'</td><td>'+b.district+'</td><td style="max-width:300px">'+b.address+'</td><td class="num">'+(b.households||'')+'</td><td><span class="badge type">'+b.building_type+'</span></td><td>'+b.mgmt_type+'</td><td>'+rt+'</td></tr>';
  }}).join('');
  const totalPages=Math.ceil(filtered.length/PER_PAGE);
  if(totalPages<=1){{pagEl.innerHTML='';return}}
  let html='<button class="page-btn" '+(page===1?'disabled':'')+' onclick="goPage('+(page-1)+')">&#8249;</button>';
  html+='<span class="page-btn active">'+page+'/'+totalPages+'</span>';
  html+='<button class="page-btn" '+(page===totalPages?'disabled':'')+' onclick="goPage('+(page+1)+')">&#8250;</button>';
  pagEl.innerHTML=html;
}}
function goPage(p){{page=p;renderCases();window.scrollTo({{top:document.getElementById('case-table').offsetTop-20,behavior:'smooth'}})}}
applyFilter();
</script>
</body>
</html>"""

with open(os.path.join(BASE, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
print(f"  dashboard.html: {len(index_html)/1024:.1f} KB")

# ========== 縣市子頁面 ==========
print("\n=== 生成縣市子頁面 ===")

for c in county_stats_sorted:
    if not c.get('has_data', True):
        print(f"  {c['county']}: 跳過（待補開放資料）")
        continue
    slug = county_slug(c['county'])
    cname = c['county']
    # 該縣市的區級資料
    c_districts = [d for d in district_stats if d['county'] == cname]
    c_districts.sort(key=lambda x: -x['total_buildings'])
    # 該縣市的個案
    c_cases = [b for b in case_db if b['county'] == cname]

    # 區級圖表資料
    dist_chart = json.dumps([{'name': d['district'], 'value': d['total_buildings'], 'hh': d['total_households']} for d in c_districts[:20]], ensure_ascii=False)

    capital_badge = '<span class="badge capital">六都</span>' if c['is_six_capital'] else '<span class="badge non-capital">非六都</span>'

    county_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cname} - 全台建案統計儀表板</title>
<link rel="stylesheet" href="https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.6.0/dist/echarts.min.js" integrity="sha384-pPi0zxBAoDu6+JXW/C68UZLvBUUtU+7zonhif43rqj7pxsGyqyqzcian2Rj37Rss" crossorigin="anonymous"></script>
<style>{CSS}</style>
</head>
<body>

<div class="header">
  <h1>{cname} 建案統計</h1>
  <div class="sub">全台建案統計儀表板 · {capital_badge} · 版本 {overview['version']}</div>
</div>

<div class="container">
  <div class="breadcrumb"><a href="../dashboard.html">首頁</a><span class="sep">/</span><span class="current">{cname}</span></div>

  <!-- KPI -->
  <div class="section">
    <div class="kpi-grid">
      <div class="kpi-card"><div class="kpi-value">{c['total_buildings']:,}</div><div class="kpi-label">報備建案總數</div><div class="kpi-note">公寓大廈報備資料</div></div>
      <div class="kpi-card accent"><div class="kpi-value">{c['total_households']:,}</div><div class="kpi-label">報備總戶數</div><div class="kpi-note">{c['buildings_with_hh']:,} 棟有戶數資料</div></div>
      <div class="kpi-card info"><div class="kpi-value">{c['district_count']}</div><div class="kpi-label">行政區數</div><div class="kpi-note">含鄉鎮市區</div></div>
      <div class="kpi-card success"><div class="kpi-value">{c['redev_zone_count']}</div><div class="kpi-label">重劃區標註</div><div class="kpi-note">依關鍵字比對</div></div>
    </div>
  </div>

  <!-- 待補指標 -->
  <div class="section">
    <div class="section-title">{cname} 建照/使照/待售/預售指標（待補開放資料）</div>
    <div class="kpi-grid">
      <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">年度建照件數</div><div class="kpi-note">含核發戶數、棟數</div></div>
      <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">年度使照件數</div><div class="kpi-note">含完工戶數、棟數</div></div>
      <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">第一次登記棟數</div><div class="kpi-note">完工登記</div></div>
      <div class="kpi-card"><div class="kpi-value pending">待補</div><div class="kpi-label">待售新成屋宅數</div><div class="kpi-note">預售屋件數/戶數待補</div></div>
    </div>
  </div>

  <!-- 區級圖表 -->
  <div class="section">
    <div class="section-title">行政區建案分布</div>
    <div class="chart-card"><div class="chart-title">各行政區建案數量 Top 20</div><div class="chart-sub">點擊柱體可篩選該區個案</div><div class="chart-container" id="chart-district" style="min-height:350px"></div></div>
  </div>

  <!-- 鄉鎮市區子表 -->
  <div class="section">
    <div class="section-title">鄉鎮市區子表（{c['district_count']} 區）</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>行政區</th><th class="num">建案數</th><th class="num">戶數</th><th>主要重劃區標註</th><th>佔比</th></tr></thead>
        <tbody>
"""
    for d in c_districts:
        redev = ', '.join(d['redev_zones'][:5]) if d['redev_zones'] else '—'
        pct = d['total_buildings'] / c['total_buildings'] * 100
        county_html += f"""          <tr><td><strong>{d['district']}</strong></td><td class="num">{d['total_buildings']:,}</td><td class="num">{d['total_households']:,}</td><td style="font-size:12px">{redev}</td><td class="num">{pct:.1f}%</td></tr>
"""

    county_html += f"""        </tbody>
      </table>
    </div>
  </div>

  <!-- 個案列表 -->
  <div class="section">
    <div class="section-title">{cname} 個案建案明細（{len(c_cases):,} 筆）</div>
    <div class="search-box"><span class="search-icon">&#128269;</span><input type="text" id="c-search" placeholder="搜尋建案名稱、地址..."></div>
    <div class="filter-row">
      <select id="c-district"><option value="">全部行政區</option></select>
      <select id="c-type"><option value="">全部型態</option><option>大樓</option><option>華廈</option><option>社區</option><option>公寓</option><option>其他</option></select>
    </div>
    <div class="result-info" id="c-result"></div>
    <div class="table-wrap">
      <table><thead><tr><th>使照序號</th><th>建案名稱</th><th>行政區</th><th>地址</th><th class="num">戶數</th><th>型態</th><th>重劃區</th></tr></thead><tbody id="c-tbody"></tbody></table>
    </div>
    <div class="pagination" id="c-pagination"></div>
  </div>

</div>

<div class="footer"><p><strong>全台建案統計儀表板</strong> · {cname} · 版本 {overview['version']}</p></div>

{make_js('DISTRICT_DATA', dist_chart)}
{make_js('CASE_DATA', json.dumps(c_cases, ensure_ascii=False))}

<script>
// 區級圖表
const cd=echarts.init(document.getElementById('chart-district'));
cd.setOption({{tooltip:{{trigger:'axis',axisPointer:{{type:'shadow'}}}},grid:{{left:'3%',right:'5%',bottom:'15%',containLabel:true}},xAxis:{{type:'category',data:DISTRICT_DATA.map(d=>d.name),axisLabel:{{rotate:45,fontSize:10}}}},yAxis:{{type:'value'}},series:[{{type:'bar',data:DISTRICT_DATA.map(d=>d.value),itemStyle:{{color:'#1a3a5c'}},barMaxWidth:30}}]}});
new ResizeObserver(()=>cd.resize()).observe(document.getElementById('chart-district'));

// 個案篩選
const PER=50;let pg=1,flt=[];
const dists=[...new Set(CASE_DATA.map(b=>b.district))].sort();
const fd=document.getElementById('c-district');
dists.forEach(d=>{{const o=document.createElement('option');o.value=d;o.textContent=d;fd.appendChild(o)}});
function applyF(){{
  const q=document.getElementById('c-search').value.trim().toLowerCase();
  const d=document.getElementById('c-district').value;
  const t=document.getElementById('c-type').value;
  flt=CASE_DATA.filter(b=>{{
    if(q&&!(b.name.toLowerCase().includes(q)||b.address.toLowerCase().includes(q)))return false;
    if(d&&b.district!==d)return false;
    if(t&&b.building_type!==t)return false;
    return true;
  }});
  pg=1;renderF();
}}
function renderF(){{
  document.getElementById('c-result').innerHTML='共 <strong>'+flt.length.toLocaleString()+'</strong> 筆';
  const s=(pg-1)*PER;const pd=flt.slice(s,s+PER);
  document.getElementById('c-tbody').innerHTML=pd.map(b=>{{
    const rt=b.redev_zone?'<span class="badge redev">'+b.redev_zone+'</span>':'';
    return '<tr><td>'+b.id+'</td><td><strong>'+b.name+'</strong></td><td>'+b.district+'</td><td style="max-width:300px">'+b.address+'</td><td class="num">'+(b.households||'')+'</td><td><span class="badge type">'+b.building_type+'</span></td><td>'+rt+'</td></tr>';
  }}).join('');
  const tp=Math.ceil(flt.length/PER);
  if(tp<=1){{document.getElementById('c-pagination').innerHTML='';return}}
  document.getElementById('c-pagination').innerHTML='<button class="page-btn" '+(pg===1?'disabled':'')+' onclick="gp('+(pg-1)+')">&#8249;</button><span class="page-btn active">'+pg+'/'+tp+'</span><button class="page-btn" '+(pg===tp?'disabled':'')+' onclick="gp('+(pg+1)+')">&#8250;</button>';
}}
function gp(p){{pg=p;renderF()}}
['c-search','c-district','c-type'].forEach(id=>{{document.getElementById(id).addEventListener('input',applyF);document.getElementById(id).addEventListener('change',applyF)}});
applyF();
</script>
</body>
</html>"""

    out_path = os.path.join(COUNTIES_DIR, f'{slug}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(county_html)
    print(f"  {cname}: {slug}.html ({len(county_html)/1024:.1f} KB, {len(c_cases):,} 筆個案)")

print(f"\n=== 全部生成完成 ===")
print(f"  主頁: {os.path.join(BASE, 'dashboard.html')}")
print(f"  縣市頁: {COUNTIES_DIR}")
