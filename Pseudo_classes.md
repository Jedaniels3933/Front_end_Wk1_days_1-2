# CSS Pseudo-classes

### What are Pseudo-classes?

#### A pseudo-class is used to define a special state of an element.
- Style an element when a user mouses over it
- Style visited and unvisited links differently
- Style an element when it gets focus

*Syntax*
The syntax of pseudo-classes:

``` selector:pseudo-class {
  property: value;
} ```

- a: link   = for un visited 
- a: visited 
- a: hover   a:hover MUST come after a:link and a:visited in the CSS definition in order to be effective
- a: active 

Note: a:hover MUST come after a:link and a:visited in the CSS definition in order to be effective.

Note: a:active MUST come after a:hover in the CSS definition in order to be effective.

## Example 

```
```
<!DOCTYPE html>
<html>
<head>
<style>
/* unvisited link */
a:link {
  color: red;
}

/* visited link */
a:visited {
  color: green;
}

/* mouse over link */
a:hover {
  color: hotpink;
}

/* selected link */
a:active {
  color: blue;
}  
```
</style>
</head>
<body>


