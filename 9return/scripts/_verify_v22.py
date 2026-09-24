# -*- coding: utf-8 -*-
import json, os
BASE = r"D:\_WWW_325\245_9return.com.tw-main"
with open(os.path.join(BASE, 'data', 'county_stats.json'), 'r', encoding='utf-8') as f:
    cs = json.load(f)
with open(os.path.join(BASE, 'data', 'district_stats.json'), 'r', encoding='utf-8') as f:
    ds = json.load(f)

print("=== county_stats (has_data) ===")
for c in cs:
    if c['has_data']:
        print(f"{c['county']}: bld={c['total_buildings']}, hh={c['total_households']}, "
              f"bld_hh={c['buildings_with_hh']}, bld_addr={c['buildings_with_addr']}, "
              f"dist={c['district_count']}, redev={c['redev_zone_count']}")
        print(f"  districts({len(c['districts'])}): {c['districts']}")
        print(f"  redev_zones({len(c['redev_zones'])}): {c['redev_zones']}")
        print(f"  mgmt_types: {c['mgmt_types']}")

print("\n=== district_stats 概況 ===")
from collections import Counter
county_dist_count = Counter(d['county'] for d in ds)
for county, cnt in county_dist_count.items():
    print(f"  {county}: {cnt} 筆")

print("\n=== 彰化縣 districts (驗證合併) ===")
for d in ds:
    if d['county'] == '彰化縣':
        print(f"  {d['district']}: bld={d['total_buildings']}, hh={d['total_households']}, redev={d['redev_zones']}")

print("\n=== 臺中市 districts (驗證無髒資料) ===")
tc_dists = [d['district'] for d in ds if d['county'] == '臺中市']
print(f"  共 {len(tc_dists)} 筆: {tc_dists}")
dirty = ["公寓大廈地址", "太平鄉新坪村10鄰育仁路112號", "潭子鄉福仁村復興路1段10號"]
for d in dirty:
    print(f"  髒資料 '{d}' {'存在!' if d in tc_dists else '已移除 ✓'}")

print("\n=== 臺北市 household 驗證 ===")
tp = [c for c in cs if c['county'] == '臺北市'][0]
print(f"  total_households = {tp['total_households']}")
print(f"  buildings_with_hh = {tp['buildings_with_hh']}")

print("\n=== JSON 格式驗證 ===")
print(f"  county_stats: {len(cs)} 縣市, JSON 有效")
print(f"  district_stats: {len(ds)} 筆, JSON 有效")
