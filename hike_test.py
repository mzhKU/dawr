import os
from scrapy.selector import Selector

# -----------------------------------------------------------------------
# 'exec(open("engine.py").read())'
# ----------------------------------------------------------------------- 

# -----------------------------------------------------------------------
# RUN
# -----------------------------------------------------------------------
if __name__ == "__main__":

    import hike_api

    # Hike reports
    hikes      = []
    POSTS_PATH = '200posts'
    files      = os.listdir(os.path.abspath(POSTS_PATH))
    raw_html   = []

    for REF in files:
        file_path = os.path.join(os.path.abspath("."), POSTS_PATH, REF)
        fh        = open(file_path, 'r')
        txt       = REF + ":::" + fh.read()
        raw_html.append(txt)
        fh.close()

    # Hike representation
    for hike_report in raw_html:
        hike_doc         = Selector(text=hike_report)
        hike             = {}
        hike["report"]   = hike_report.split(":::")[0]
        hike["title"]    = hike_api.get_hike_title(hike_doc)
        hike["region"]   = hike_api.get_hike_region(hike_doc)
        hike["level"]    = hike_api.get_hike_difficulty(hike_doc)
        hike["comments"] = hike_api.get_number_of_comments(hike_doc)
        hikes.append(hike)

    # print_hike_list_with_title(hikes, title="Pizzo")
    regions = hike_api.get_regions(hikes)
    print(regions) 
    # hike_api.print_hike_list_with_region(hikes, region="Luzern")
    # print(get_regions(hikes))
# -----------------------------------------------------------------------
