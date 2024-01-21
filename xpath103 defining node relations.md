axes

* ancestor axis
selects all parent nodes of a given node, up to the root node

* select every ul node but it has no attribute
we can still select ul given a descendant node
eg. //span[@class="title"]/ancestor::ul

* note that ancestor will match all the specified nodes up to the root node
so if we have another ul node as one of the parents for span nodes
, then that ul will also be returned
use //span[@class="title"]/ancestor::ul[1] to select 


side note: shouldn't depend much on position of an HTML element on a page
as some pages update generated content



* parent axis
restrict the match to only the first ancestor

eg. select immediate parent of span element which is li
use //span[@class="title"]/parent::li


* child axis
selects the immedate child of a given node
eg. assuming span that contains the book's price does not have a class or attribute
but li has class = book
//li[@class="book"]/child::span[@class="price"]


* descendant axis
if we want to select all the grandchildren
//ul/descendant::span[@class="price"]
equivalent to //ul//span[@class="price"]


* following axis
selects specified nodes following the closing tag of a given current node

        <li class="book">
          <span class="title">Harry Potter</span>
          <span class="author">J K. Rowling</span>
          <span class="year">2005</span>
          <span class="price">29.99</span>
        </li>
        <li>
          <span class="title">The Golden Compass</span>
          <span class="author">Phillip Collman</span>
          <span class="year">2001</span>
          <span class="price">25.99</span>
        </li>
        <li>
          <span class="title">The Magicians</span>
          <span class="author">Lev Grossman</span>
          <span class="year">2015</span>
          <span class="price">45.99</span>
        </li>

suppose every book has some header info not of interest
we want to skip this data and select only date after this

eg. match nodes that come after the first instance of the specified li node
//li[@class="book"]/following::span


* following-sibling axis
same function as following but restrict the selection to siblings under the specified parent node

eg. select the span nodes under div node for header only

    <div>
      <div class="header"> our book list </div>
      <span> this list contains all books on sale </span>
      <span> we hope you like it </span>
    </div>

//div[@class="header"]/following-sibling::span


* preceding axis
select all preceding nodes in the same level as the specified current node
but do not necessarily share the same parent
eg. //span[@class="price"]/preceding::span

* preceding-sibling axis
same as preceding, but limit selection to only nodes that share the same parent

eg. //span[@class="price"]/preceding-sibling::span