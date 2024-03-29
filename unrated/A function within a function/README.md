# [A function within a function](https://www.codewars.com/kata/53844152aa6fc137d8000589)
Given an input n, write a function `always` that returns a __function__ which returns n. Ruby should return a __lambda__ or a __proc__.

```javascript
var three = always(3);
three(); // returns 3
```
```coffeescript
three = always(3)
three() # returns 3
```
```ruby
three = always(3)
three.call # returns 3
```
```python
three = always(3)
three() /* returns 3 */
```
```haskell
let three = always 3
three () -- returns 3
```
```clojure
(def three (always 3))
(three) ;; returns 3
```
```elixir
three = always(3)
three.() #=> 3
```
```cpp
function<int (void)> three = always(3);
three(); // returns 3
```
```csharp
Func<int> three = Kata.Always(3);
three(); // returns 3
```