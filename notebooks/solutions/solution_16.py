
science_doc = {
    "Agricultural sciences": 1065,
    "Biochemistry": 759,
    "Molecular biology": 716,
    "Neurosciences": 431,
    "Other biological sciences": 3675,
    "Computer sciences": 856,
    "Earth, atmospheric, and ocean sciences": 706,
    "Mathematics": 1083,
    "Chemistry": 2132,
    "Physics and astronomy": 715,
    "Astrology": 2012,
    "Psychology": 3668,
    "Social sciences": 4063,
}

engineering_doc = {
    "Aerospace/aeronautical engineering": 206,
    "Chemical engineering": 576,
    "Civil engineering": 506,
    "Electrical engineering": 1236,
    "Industrial/manufacturing engineering": 211,
    "Materials science engineering": 393,
    "Mechanical engineering": 786,
    "Other engineering": 1416,
}

humanities_doc = {
    "Foreign languages and literature": 626,
    "History": 960,
    "Letters": 1516,
    "Other humanities": 1934,
}

# 1. Merge the 3 dictionaries
# ***************************
all_doc = {}
all_doc.update(science_doc)
all_doc.update(engineering_doc)
all_doc.update(humanities_doc)
print(all_doc)

# Alternatively, we could also copy one of the dict as a starting point
# with the "copy()" method of dict:
all_doc_2 = science_doc.copy()
all_doc_2.update(engineering_doc)
all_doc_2.update(humanities_doc)
print("Are the two dict identical?", all_doc == all_doc_2)

# python > 3.5 ** dictionary unpacking.
all_doc_3 = {**science_doc, **engineering_doc, **humanities_doc}


# 2. What is the length of the all_doc dictionnary
# ************************************************
print("Length of the dictionary:", len(all_doc))


# 3. Add "Health" doctorates
# **************************
all_doc["Health"] = 1407


# 4. Multiply by 2 the number of "Physics and astronomy" doctorates
# *****************************************************************
key = "Physics and astronomy"
print(key, ":", all_doc[key])
all_doc[key] = all_doc[key] * 2  # Alternatively: all_doc[key] *= 2
print(key, ":", all_doc[key])


# 5. Remove the "Astrology" key
# *****************************
all_doc.pop("Astrology")
print(all_doc)
