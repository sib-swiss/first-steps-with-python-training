# Exercise 2.4

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
# The easiest way to complete this task is using the dict union operator: |
all_doc = science_doc | engineering_doc | humanities_doc

# Alternatively, we can also copy one of the dict as a starting point, and
# then update it inplace with the content of the other two dicts.
all_doc = science_doc.copy()
all_doc.update(engineering_doc)
all_doc.update(humanities_doc)

# Or we can use dictionary unpacking.
all_doc = {**science_doc, **engineering_doc, **humanities_doc}


# 2. Length of the all_doc dictionary
# ***********************************
print("Length of the dictionary:", len(all_doc))


# 3. Add "Health" doctorates
# **************************
all_doc["Health"] = 1407


# 4. Multiply by 2 the number of "Physics and astronomy" doctorates
# *****************************************************************
all_doc["Physics and astronomy"] *= 2
print(all_doc["Physics and astronomy"])


# 5. Remove the "Astrology" key
# *****************************
all_doc.pop("Astrology")
print(all_doc)
