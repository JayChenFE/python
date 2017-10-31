# 16-5
# 涵盖所有国家 ：
# 本节制作人口地图时，对于大约12个国家，程序不能自动确定其两个字母的国别码。
# 请找出这些国家，在字典COUNTRIES 中找到它们的国别码；
# 然后，对于每个这样的国家，都在get_country_code() 中添加一个if-elif 代码块，
# 以返回其国别码：
# if country_name == 'Yemen, Rep.'
# return 'ye'
# elif --snip--
# 将这些代码放在遍历COUNTRIES 的循环和语句return None 之间。
# 完成这样的修改后，你看到的地图将更完整。

import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

from country_codes import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RS('#336699',base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')
