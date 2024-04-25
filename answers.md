# CMPS 2200 Recitation 08

## Answers

**Name:**______Basil Mustafa___________________
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
Work is O(V + ElogV) where 'V' is the number of vertices and 'E' is the number of edges



- **2b)**
path = []

while parents[destination] is not None: path.append(parents[destination]) destination = parents[destination]

return ''.join(path[::-1])

