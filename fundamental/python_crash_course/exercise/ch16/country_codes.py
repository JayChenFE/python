from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    local_codes = {'Yemen, Rep.': 'ye'}
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name in local_codes.keys():
        return local_codes[country_name]
    # print(country_name)
    return None
