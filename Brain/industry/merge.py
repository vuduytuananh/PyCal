from PyCal.Memory.data_factory import DataFactory
def get_lower_industry_level(sub_industry):
    industry_hierarchy = ["Domain", "Sub-Domain", "Category", "Sub-Category"]
    sub_industry_lower_level = ""
    sub_industry_level = industry_hierarchy.index(sub_industry)
    if sub_industry_level == 3: raise Exception("@Vu --> there is no lowver industry level of Industry/Sub-Category")
    else: sub_industry_lower_level = industry_hierarchy[sub_industry_level + 1]
    return sub_industry_lower_level
def merge(a_out, b_out):
    merged = {}
    for k in set(a_out) | set(b_out):
        k_set = set()
        if k in a_out:
            k_set.update(a_out)
            if k in b_out:
                k_set.update(b_out)
        else:
            k_set.update(b_out)
        merged[k] = k_set
    return merged

def count_lower_level(sub_industry, sub_industry_value):
    sub_industry_lower_level = get_lower_industry_level(sub_industry)
    data_factory = DataFactory()
    industry_ref = data_factory.getTab("ReferenceTab", "Industry Tree", {sub_industry: [sub_industry_value], sub_industry_lower_level: []})
    count = len(set(industry_ref[sub_industry_lower_level].values))
    return count
