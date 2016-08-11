# it2i

Replace Latex italics with HTML italics.

Convenient for quickly preparing Latex content for an HTML page with default MathJax.

### Example

Input:  \textit{string}

Output: &lt;i&gt;string&lt;\i&gt;

### Note

* Only works when no other curly braces appear inside \textit{}.
* This is not a converter from Latex to HTML. It replaces italics and nothing else.

### Usage 

`python it2i.py [path to input text file] [path to output text file]`
