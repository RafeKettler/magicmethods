#A Guide to Python's Magic Methods#

###Rafe Kettler###

Copyright &copy; 2012 Rafe Kettler

Version 1.14

A PDF version of this guide can be obtained from [my site](http://www.rafekettler.com/magicmethods.pdf) or [Github](https://github.com/RafeKettler/magicmethods/raw/master/magicmethods.pdf). The magic methods guide has [a git repository at http://www.github.com/RafeKettler/magicmethods](http://www.github.com/RafeKettler/magicmethods). Any issues can be reported 
there, along with comments, (or even contributions!).

**<a id="table" href="#table">Table of Contents</a>**


 1. [Introduction](#intro)
 2. [Construction and Initialization](#construction)
 3. [Making Operators Work on Custom Classes](#operators)
    - [Comparison magic methods](#comparisons)
    - [Numeric magic methods](#numeric)
 4. [Representing your Classes](#representations)
 5. [Controlling Attribute Access](#access)
 6. [Making Custom Sequences](#sequence)
 7. [Reflection](#reflection)
 8. [Callable Objects](#callable)
 9. [Context Managers](#context)
 10. [Building Descriptor Objects](#descriptor)
 11. [Copying](#copying)
 12. [Pickling your Objects](#pickling)
 13. [Conclusion](#conclusion)
 14. [Appendix: How to Call Magic Methods](#appendix)