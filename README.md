# it2i

Replace Latex italics with HTML italics.

Convenient for quickly preparing Latex content for an HTML page with default MathJax.

### Example

Input:  \textit{string}

Output: &lt;i&gt;string&lt;\i&gt;

### Note

Only works when no other curly braces appear inside \textit{}.

### Usage 

`python it2i.py [input .tex file] [output .html file]`
