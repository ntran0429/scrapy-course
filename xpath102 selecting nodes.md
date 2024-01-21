XML files contain of nodes
parent vs child nodes, attribute of a node to add context to the node
atomic nodes don't have children and don't belong to parents either
parents tree of a given node refers to node ancestors
children tree of a given parent refers to node desendants



xpath 102 (refer to the cheat sheet and html sample)

/ to start at the root node

//span[@class="title"] selects span nodes with this specific class


* *ut the query output in scrapy's xpath will not contain the text inside the span nodes
, but rather the span nodes themselves
we will need to extract the data inside the nodes

eg. 
<span class="title">Harry Potter</span>
<span class="title">The Golden Compass</span>
<span class="title">The Magicians</span>
<span class="title">The Lightning Thief</span>


* to extract the text in this example:
//span[@class="title"]/text()

* this query can be at the start of in between node selectors
eg. we want to get data starting from the ul node to the span node
, don't care about any nodes in between
//ul//span[@class="title"]/text()


* select all nodes with attribute @id
//@id returns all nodes with this attribute


* select a specific book title based on the order in the list
for this, we need to include the li node as the parent
eg. //li[1]//span[@class="title"]
to get the first book title in the list

eg. //li[last()]//span[@class="title"]
selects the last book title

eg. //li[position() < 3]//span[@class="title"]


* what if the data we want are not in one consistent node type
ie. some nodes are span, some are div
eg. //*[@class="title"] to select nodes with attribute of class = "title"

<li class="book">
    <div class="title">Harry Potter</div>
    <span class="author">J K. Rowling</span>
    <span class="year">2005</span>
    <span class="price">29.99</span>
</li>

but be careful because there might be some nodes with that same attribute but
do not store book data


using pip operator to combine more than one query
eg. //span[@class="title"]/text() | //div[@class="title"]/text()