import pycountry

options = ""
country_list = ['ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr','hk','hu','id','in','ie','il','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph','pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us','ve','za']
for country in pycountry.countries:
    for i in country_list:
        if(country.alpha_2.lower()==i):
            i==country
            options += f'<option value="{country.alpha_2.lower()}">{country.name}</option>\n'

select_list = f'<select id="myList" name="myList">\n{options}</select>'

print(select_list)