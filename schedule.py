"""
file: store_location.py
author: Nick Duggan nkd2840@rit.edu
course: csci141
assignment:lab06
language:python
date: 10/23/22

"""
from dataclasses import dataclass


@dataclass
class Project:
    name: str
    length: int
    revenue: int

def get_proj_names(file):
    projects = dict()
    count = 1
    with open(file) as fp:
        for line in fp:
            name, length, revenue = line.split()
            project = Project(name, length, revenue)
            print(name)
            print(length)
            print(revenue)
            if name not in projects:
                projects[count] = project
                count += 1

    return projects

# def insertion_sort(projects):
#     for p in projects:
#         sorted_values = sorted(p.length())  # Sort the values
#         sorted_dict = {}
#
#         for i in sorted_values:
#             for k in p.keys():
#                 if p[k] == i:
#                     sorted_dict[k] = p[k]
# def insertion_sort(projects):
#     sorted = {}
#     for p in projects:
#         sorted += projects[p]
#         print(sorted)
#         for i in sorted:
#             value = sorted[i]
#             while i > 0 and value.length < sorted[i - 1].length:
#                 print(sorted[i])
#                 sorted[i] = sorted[i - 1]
#                 print(sorted[i])
#                 i = i - 1
#             sorted[i] = value


# def insertion_sort(projects):
#     totals = {}
#
#     for project in projects.values():
#         print(project)
#         for project.name in project:
#             while project.length <
#             # if box.cookie not in totals:
#             #     totals[box.cookie] = box.count
#             # else:
#             #     totals[box.cookie] += box.count

    # return totals
# def insertion_sort(data):
#
#     for index in range(1, len(data)):
#
#         value = data[index].length
#
#         j = index
#         while j > 1 and value < data[j - 1].length:
#             print("b",data[j])
#             data[j] = data[j - 1]
#             print("a",data[j])
#             j = j - 1
#         data[j] = value
#         print(data)


def main():
    file = input("input file: ")
    proj = get_proj_names(file)
    for p in proj:
        print(proj[p])
    print(proj)
    print(insertion_sort(proj))

main()