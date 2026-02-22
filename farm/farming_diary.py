"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
from farm.rice import Rice

print("\n\n📝 Day One: Corn")

corn = Corn()
corn.water()
print(f"The corn crop produced {corn.grains} grains")
print("The corn crop is ripe" if corn.ripe() else "The corn crop is not ripe")



print("\n\n📝 Day Two: Rice")

rice = Rice()
rice.water()
rice.transplant()
print(f"The rice crop produced {rice.grains} grains")
print("The rice crop is ripe" if rice.ripe() else "The rice crop is not ripe")
