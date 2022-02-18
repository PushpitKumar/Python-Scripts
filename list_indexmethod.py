#Index method returns the index of first occurence of the object.
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index('m'))
print(music.index('your'))
print(bio.index('Metatarsal'))
print(bio.index([]))
print(bio.index(43))
print(bio.index(0)) #0 is not present in bio therefore we'll get a traceback
