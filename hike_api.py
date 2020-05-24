# import os
# from scrapy.selector import Selector

# -----------------------------------------------------------------------
# FEATURE EXTRACTION API
# -----------------------------------------------------------------------
selector_title   = 'h1.title::text'
selector_level   = 'table.fiche_rando tr:nth-of-type(3) td:nth-of-type(2) a::text'
selector_region  = 'table.fiche_rando tr:first-of-type td:last-of-type a:last-of-type::text'
selector_menu    = '#sidebar_swiss div.menu_right li'
selector_comment = '#sidebar_swiss li:last-of-type a::text'

def get_hike_title(hike_doc):
    return hike_doc.css(selector_title).get()

def get_hike_region(hike_doc):
    region = hike_doc.css(selector_region).get()
    return region

def get_hike_difficulty(hike_doc):
    """
    T1: Wandern
    T2: Bergwandern
    T3: Anspruchsvolles Bergwandern
    T4: Alpinwandern
    T5: Anspruchsvolles Alpinwandern
    T6: Schwieriges Alpinwandern
    Returns 'T1', 'T2', ... 
    """
    t_level = hike_doc.css(selector_level).get()
    return t_level.split('-')[0].strip()

# Returns an integer representing the number of comments.
def get_number_of_comments(hike_doc): 
    sidebar_menu = hike_doc.css(selector_menu).getall() 
    # If there are comments the menu has 4 li tags.
    if (len(sidebar_menu) == 4):
        comment_tag = hike_doc.css(selector_comment).get()
        return get_comment_count(comment_tag)
    else:
        return 0

def get_regions(hikes):
    return list(map(lambda d: d['region'], hikes))

def get_comment_count(a):
    count = a.split("Kommentare")[-1].split("(")[-1].split(")")[0]
    return int(count)

def print_hike_list_with_title(hikes, title):
    for h in hikes:
        if (title in h["title"]):
            print(h)

def print_hike_list_with_region(hikes, region):
    for h in hikes:
        if (region in h["region"]):
            print(h) 
# ----------------------------------------------------------------------- 
