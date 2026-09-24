# -*- coding: utf-8 -*-
"""
資料清理腳本 v2.2
- 修復 county_stats.json 各縣市髒資料
- 修復 district_stats.json 對應清理
- 更新 overview.json 彙總數字
"""
import json, os, copy

BASE = r"D:\_WWW_325\245_9return.com.tw-main"
DATA_DIR = os.path.join(BASE, "data")

# ========== 讀取 ==========
with open(os.path.join(DATA_DIR, 'county_stats.json'), 'r', encoding='utf-8') as f:
    county_stats = json.load(f)
with open(os.path.join(DATA_DIR, 'district_stats.json'), 'r', encoding='utf-8') as f:
    district_stats = json.load(f)
with open(os.path.join(DATA_DIR, 'overview.json'), 'r', encoding='utf-8') as f:
    overview = json.load(f)

# 記錄清理前後對照
before_after = {}

def get_county(name):
    for c in county_stats:
        if c['county'] == name:
            return c
    return None

# ========== 各縣市 redev_zone 保留清單 ==========
REDEV_KEEP = {
    "臺中市": {"七期","八期","九期","十期","十一期","十二期","十三期","十四期",
              "水湳","高鐵","捷運","北屯","南屯","西屯","大坑","廍子","太平","大里",
              "工業區","新市鎮","湖濱","河濱","科學園區","中山","中正","大安","復興"},
    "彰化縣": {"工業區","新市","濱海"},
    "嘉義市": {"復興"},
    "臺北市": {"中山","中正","信義","內湖","北投","南港","士林","大同","大安",
              "捷運","文山","松山","萬華"},
    "新北市": {"三峽","三重","中和","五股","土城","工業區","捷運","新莊","板橋",
              "林口","樹林","永和","淡海","蘆洲","頂埔"},
    "桃園市": {"A18","A19","中壢","八德","復興","捷運","青埔","高鐵"},
    "新竹市": {"寶山","復興","新竹","濱海","香山"},
    "臺南市": {"仁德","安南","安平","新市","歸仁","永康","高鐵"},
}

# ========== 1. 臺中市 ==========
tc = get_county("臺中市")
before_after["臺中市"] = {"district_count": [tc["district_count"], None],
                           "redev_zone_count": [tc["redev_zone_count"], None]}

# districts: 移除3個髒資料
dirty_districts_tc = {"公寓大廈地址", "太平鄉新坪村10鄰育仁路112號", "潭子鄉福仁村復興路1段10號"}
tc["districts"] = [d for d in tc["districts"] if d not in dirty_districts_tc]
tc["district_count"] = len(tc["districts"])

# mgmt_types: 只保留管理委員會和管理負責人
tc["mgmt_types"] = {k: v for k, v in tc["mgmt_types"].items()
                     if k in ("管理委員會", "管理負責人")}

# redev_zones: 過濾
tc["redev_zones"] = [z for z in tc["redev_zones"] if z in REDEV_KEEP["臺中市"]]
tc["redev_zone_count"] = len(tc["redev_zones"])

before_after["臺中市"]["district_count"][1] = tc["district_count"]
before_after["臺中市"]["redev_zone_count"][1] = tc["redev_zone_count"]
print(f"[臺中市] districts: {before_after['臺中市']['district_count'][0]}→{tc['district_count']}, "
      f"redev_zones: {before_after['臺中市']['redev_zone_count'][0]}→{tc['redev_zone_count']}")

# ========== 2. 彰化縣 ==========
ch = get_county("彰化縣")
before_after["彰化縣"] = {"district_count": [ch["district_count"], None],
                           "redev_zone_count": [ch["redev_zone_count"], None]}

# districts: 去重，保留有後綴的版本
changhua_pairs = {
    "二林": "二林鎮", "伸港": "伸港鄉", "北斗": "北斗鎮", "和美": "和美鎮",
    "員林": "員林市", "埔心": "埔心鄉", "埔鹽": "埔鹽鄉", "埤頭": "埤頭鄉",
    "大村": "大村鄉", "彰化": "彰化市", "永靖": "永靖鄉", "溪湖": "溪湖鎮",
    "田中": "田中鎮", "社頭": "社頭鄉", "福興": "福興鄉", "秀水": "秀水鄉",
    "竹塘": "竹塘鄉", "花壇": "花壇鄉", "芳苑": "芳苑鄉", "鹿港": "鹿港鎮",
}
short_names = set(changhua_pairs.keys())
ch["districts"] = [d for d in ch["districts"] if d not in short_names]
ch["district_count"] = len(ch["districts"])

# redev_zones: 過濾
ch["redev_zones"] = [z for z in ch["redev_zones"] if z in REDEV_KEEP["彰化縣"]]
ch["redev_zone_count"] = len(ch["redev_zones"])

before_after["彰化縣"]["district_count"][1] = ch["district_count"]
before_after["彰化縣"]["redev_zone_count"][1] = ch["redev_zone_count"]
print(f"[彰化縣] districts: {before_after['彰化縣']['district_count'][0]}→{ch['district_count']}, "
      f"redev_zones: {before_after['彰化縣']['redev_zone_count'][0]}→{ch['redev_zone_count']}")

# ========== 3. 嘉義市 ==========
cy = get_county("嘉義市")
before_after["嘉義市"] = {"district_count": [cy["district_count"], None],
                           "redev_zone_count": [cy["redev_zone_count"], None]}

# mgmt_types: 管理委員(2) 併入 管理委員會
if "管理委員" in cy["mgmt_types"]:
    cy["mgmt_types"]["管理委員會"] = cy["mgmt_types"].get("管理委員會", 0) + cy["mgmt_types"]["管理委員"]
    del cy["mgmt_types"]["管理委員"]

# redev_zones: 過濾
cy["redev_zones"] = [z for z in cy["redev_zones"] if z in REDEV_KEEP["嘉義市"]]
cy["redev_zone_count"] = len(cy["redev_zones"])

before_after["嘉義市"]["district_count"][1] = cy["district_count"]
before_after["嘉義市"]["redev_zone_count"][1] = cy["redev_zone_count"]
print(f"[嘉義市] districts: {cy['district_count']} (不變), "
      f"redev_zones: {before_after['嘉義市']['redev_zone_count'][0]}→{cy['redev_zone_count']}, "
      f"mgmt: 管理委員會={cy['mgmt_types']['管理委員會']}")

# ========== 4. 臺北市 ==========
tp = get_county("臺北市")
before_after["臺北市"] = {"district_count": [tp["district_count"], None],
                           "redev_zone_count": [tp["redev_zone_count"], None]}

# total_households 異常 → null
tp["total_households"] = None
tp["buildings_with_hh"] = None

# redev_zones: 過濾
tp["redev_zones"] = [z for z in tp["redev_zones"] if z in REDEV_KEEP["臺北市"]]
tp["redev_zone_count"] = len(tp["redev_zones"])

before_after["臺北市"]["district_count"][1] = tp["district_count"]
before_after["臺北市"]["redev_zone_count"][1] = tp["redev_zone_count"]
print(f"[臺北市] districts: {tp['district_count']} (不變), "
      f"redev_zones: {before_after['臺北市']['redev_zone_count'][0]}→{tp['redev_zone_count']}, "
      f"total_households: 302→null")

# ========== 5. 新北市 ==========
nt = get_county("新北市")
before_after["新北市"] = {"district_count": [nt["district_count"], None],
                           "redev_zone_count": [nt["redev_zone_count"], None]}

nt["redev_zones"] = [z for z in nt["redev_zones"] if z in REDEV_KEEP["新北市"]]
nt["redev_zone_count"] = len(nt["redev_zones"])

before_after["新北市"]["district_count"][1] = nt["district_count"]
before_after["新北市"]["redev_zone_count"][1] = nt["redev_zone_count"]
print(f"[新北市] districts: {nt['district_count']} (不變), "
      f"redev_zones: {before_after['新北市']['redev_zone_count'][0]}→{nt['redev_zone_count']}")

# ========== 6. 桃園市 ==========
ty = get_county("桃園市")
before_after["桃園市"] = {"district_count": [ty["district_count"], None],
                           "redev_zone_count": [ty["redev_zone_count"], None]}

ty["redev_zones"] = [z for z in ty["redev_zones"] if z in REDEV_KEEP["桃園市"]]
ty["redev_zone_count"] = len(ty["redev_zones"])

before_after["桃園市"]["district_count"][1] = ty["district_count"]
before_after["桃園市"]["redev_zone_count"][1] = ty["redev_zone_count"]
print(f"[桃園市] districts: {ty['district_count']} (不變), "
      f"redev_zones: {before_after['桃園市']['redev_zone_count'][0]}→{ty['redev_zone_count']}")

# ========== 7. 新竹市 ==========
hc = get_county("新竹市")
before_after["新竹市"] = {"district_count": [hc["district_count"], None],
                           "redev_zone_count": [hc["redev_zone_count"], None]}

hc["redev_zones"] = [z for z in hc["redev_zones"] if z in REDEV_KEEP["新竹市"]]
hc["redev_zone_count"] = len(hc["redev_zones"])

before_after["新竹市"]["district_count"][1] = hc["district_count"]
before_after["新竹市"]["redev_zone_count"][1] = hc["redev_zone_count"]
print(f"[新竹市] districts: {hc['district_count']} (不變), "
      f"redev_zones: {before_after['新竹市']['redev_zone_count'][0]}→{hc['redev_zone_count']}")

# ========== 8. 臺南市 ==========
tn = get_county("臺南市")
before_after["臺南市"] = {"district_count": [tn["district_count"], None],
                           "redev_zone_count": [tn["redev_zone_count"], None]}

tn["redev_zones"] = [z for z in tn["redev_zones"] if z in REDEV_KEEP["臺南市"]]
tn["redev_zone_count"] = len(tn["redev_zones"])

before_after["臺南市"]["district_count"][1] = tn["district_count"]
before_after["臺南市"]["redev_zone_count"][1] = tn["redev_zone_count"]
print(f"[臺南市] districts: {tn['district_count']} (不變), "
      f"redev_zones: {before_after['臺南市']['redev_zone_count'][0]}→{tn['redev_zone_count']}")

# ========== district_stats.json 清理 ==========
print("\n=== district_stats 清理 ===")

# 臺中市: 移除髒行政區記錄
tc_dirty = {"公寓大廈地址", "太平鄉新坪村10鄰育仁路112號", "潭子鄉福仁村復興路1段10號"}
removed_tc = [d for d in district_stats if d["county"] == "臺中市" and d["district"] in tc_dirty]
district_stats = [d for d in district_stats
                   if not (d["county"] == "臺中市" and d["district"] in tc_dirty)]
print(f"  臺中市移除 {len(removed_tc)} 筆髒行政區記錄: {[r['district'] for r in removed_tc]}")

# 彰化縣: 合併無後綴版本到有後綴版本
for short, full in changhua_pairs.items():
    short_rec = next((d for d in district_stats if d["county"] == "彰化縣" and d["district"] == short), None)
    full_rec = next((d for d in district_stats if d["county"] == "彰化縣" and d["district"] == full), None)
    if short_rec and full_rec:
        full_rec["total_buildings"] += short_rec["total_buildings"]
        full_rec["total_households"] += short_rec["total_households"]
        # redev_zones 合併去重
        merged_zones = list(dict.fromkeys(full_rec["redev_zones"] + short_rec["redev_zones"]))
        full_rec["redev_zones"] = merged_zones
        # 移除 short 記錄
        district_stats = [d for d in district_stats
                           if not (d["county"] == "彰化縣" and d["district"] == short)]
print(f"  彰化縣合併 {len(changhua_pairs)} 對重複行政區")

# 所有縣市: 過濾 district_stats 中的 redev_zones
for d in district_stats:
    county = d["county"]
    if county in REDEV_KEEP:
        d["redev_zones"] = [z for z in d["redev_zones"] if z in REDEV_KEEP[county]]
print(f"  已過濾所有縣市 district 級 redev_zones")

# ========== overview.json 更新 ==========
print("\n=== overview.json 更新 ===")
overview["version"] = "v2.2"
overview["timestamp"] = "2026-09-07"

has_data_counties = [c for c in county_stats if c.get("has_data", False)]
overview["total_buildings"] = sum(c["total_buildings"] for c in has_data_counties)
overview["total_households"] = sum(c["total_households"] for c in has_data_counties
                                     if c["total_households"] is not None)
overview["total_districts"] = sum(c["district_count"] for c in has_data_counties)
overview["redev_count"] = sum(c["redev_zone_count"] for c in has_data_counties)
overview["buildings_with_addr"] = sum(c["buildings_with_addr"] for c in has_data_counties
                                        if c["buildings_with_addr"] is not None)
overview["buildings_with_hh"] = sum(c["buildings_with_hh"] for c in has_data_counties
                                      if c["buildings_with_hh"] is not None)

print(f"  total_buildings: {overview['total_buildings']}")
print(f"  total_households: {overview['total_households']}")
print(f"  total_districts: {overview['total_districts']}")
print(f"  redev_count: {overview['redev_count']}")
print(f"  buildings_with_addr: {overview['buildings_with_addr']}")
print(f"  buildings_with_hh: {overview['buildings_with_hh']}")

# ========== 寫入檔案 ==========
with open(os.path.join(DATA_DIR, 'county_stats.json'), 'w', encoding='utf-8') as f:
    json.dump(county_stats, f, ensure_ascii=False, indent=2)

with open(os.path.join(DATA_DIR, 'district_stats.json'), 'w', encoding='utf-8') as f:
    json.dump(district_stats, f, ensure_ascii=False, indent=2)

with open(os.path.join(DATA_DIR, 'overview.json'), 'w', encoding='utf-8') as f:
    json.dump(overview, f, ensure_ascii=False, indent=2)

print("\n=== 全部檔案已寫入 ===")
print(f"  county_stats.json: {len(county_stats)} 縣市")
print(f"  district_stats.json: {len(district_stats)} 筆區級記錄")
print(f"  overview.json: version={overview['version']}")
