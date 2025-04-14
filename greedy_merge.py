def greedy_merge(fragments): # Merges fragments using a greedy algorithm
    while len(fragments) > 1:
        print ("Testing fragments...")
        for i in range(len(fragments)):
            print ("s" + str(i) + ":", fragments[i])
        print ()
        
        max_overlap = 0
        best_pair = (0, 1)
        best_overlap = ""
        
        # Find a pair with the maximum overlap
        for i in range(len(fragments)):
            for j in range(len(fragments)):
                if i != j:
                    overlap = find_overlap(fragments[i], fragments[j])
                    if len(overlap) > max_overlap:
                        max_overlap = len(overlap)
                        best_pair = (i, j)
                        best_overlap = overlap

        i, j = best_pair
        fragment1 = fragments[i]
        fragment2 = fragments[j]

        # Remove both fragments from the list
        fragments.pop(max(i, j))
        fragments.pop(min(i, j))

        # Merge the two fragments based on overlap
        merged = merge_fragments(fragment1, fragment2, best_overlap)

        print(f"Merged: '{fragment1}' + '{fragment2}' = '{merged}'")
        print()
        fragments.append(merged)

    return fragments[0]

def find_overlap(fragment1, fragment2): # Finds the longest overlap between two fragments
    max_overlap_len = 0
    overlap = ""
    for i in range(1, len(fragment1)):
        if fragment2.startswith(fragment1[i:]): # Check if fragment2 starts with a substring of fragment1 as fragment1 is iterated
            overlap_len = len(fragment1) - i
            if overlap_len > max_overlap_len:
                max_overlap_len = overlap_len
                overlap = fragment1[i:]
    return overlap

def merge_fragments(fragment1, fragment2, overlap): # Merge two fragments based on the overlap
    merged_fragment = fragment1 + fragment2[len(overlap):]
    return merged_fragment

# def test(fragments): # This function is a placeholder for testing purposes (deprecated)
#     print ("Testing fragments...")
#     for i in range(len(fragments)):
#         print ("s" + str(i) + ":", fragments[i])
#     print ()

#     for i in range(len(fragments)):
#         for j in range(i + 1, len(fragments)):
#             overlap = find_overlap(fragments[i], fragments[j])
#             if overlap:
#                 merged_fragment = merge_fragments(fragments[i], fragments[j], overlap)
#                 # fragments[i] = merged_fragment
#                 print ("Found match:", "'" + fragments[i] + "'", "with", "'" + fragments[j] + "'")
#                 print ("Overlap:", overlap)
#                 fragments.pop(j)
#                 fragments.append(merged_fragment)
#                 break

#     result = fragments
#     return result

def main():
    print ("===========START=============")
    fragments = ["all is well", "ell that en", "hat end", "t ends well"]
    # result = test(fragments)
    result = greedy_merge(fragments)
    print ("Result:", result)
    print ("============END==============")
main()