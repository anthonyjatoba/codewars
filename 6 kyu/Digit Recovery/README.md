# [Digit Recovery](https://www.codewars.com/kata/5964d7e633b908e172000046)
<h2>Digit Recovery</h2>

Some letters in the input string are representing a written-out digit. Some of the letters may randomly shuffled. Your task is to recover them all.

Note that:
<ul>
<li> Only consecutive letters can be used. "OTNE" cannot be recovered to 1!
<li> Every letter has to start with an increasing index.. "ONENO" results to 11, because the E can be used two times. Endless loops are not possible!</li>
<li> If there are letters in the string, which don't create a number you can ignore them.</li>
<li> If no digits can be found, return <code>"No digits found"</code></li>
<li> Take care about the order! "ENOWT" will be recovered to 12 and not to 21.</li>
<li> The input string consists only UpperCase letters </li>
</ul>

e.g.

<pre>
<code>
recover("NEO") =>  "1"
recover("ONETWO") => "12"
recover("ONENO") => "11"
recover("TWWTONE") => "21"
recover("ZYX") => "No digits found"
recover("NEOTWONEINEIGHTOWSVEEN") => "12219827"
</code>
</pre>

You can use the following preloaded dictionary in your solution:
<pre>
<code>
const alph = {"ZERO":0,"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9};
</code>
</pre>