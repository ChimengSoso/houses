<main class="col-md markdown-body">

<h1 id="houses">Houses</h1>

<p>Implement a program to import student data into a database, and then produce class rosters.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python import.py characters.csv
$ python roster.py Gryffindor

Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
</code></pre></div></div>

<h2 id="getting-started">Getting Started</h2>

<p>Here’s how to download this problem into your own CS50 IDE. Log into <a href="https://ide.cs50.io/">CS50 IDE</a> and then, in a terminal window, execute each of the below.</p>

<ul>
  <li data-marker="*">Execute <code class="highlighter-rouge">cd</code> to ensure that you’re in <code class="highlighter-rouge">~/</code> (i.e., your home directory, aka <code class="highlighter-rouge">~</code>).</li>
  <li data-marker="*">If you haven’t already, execute <code class="highlighter-rouge">mkdir pset7</code> to make (i.e., create) a directory called <code class="highlighter-rouge">pset7</code> in your home directory.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">cd pset7</code> to change into (i.e., open) that directory.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">wget https://cdn.cs50.net/2019/fall/psets/7/houses/houses.zip</code> to download a (compressed) ZIP file with this problem’s distribution.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">unzip houses.zip</code> to uncompress that file.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">rm houses.zip</code> followed by <code class="highlighter-rouge">yes</code> or <code class="highlighter-rouge">y</code> to delete that ZIP file.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">ls</code>. You should see a directory called <code class="highlighter-rouge">houses</code>, which was inside of that ZIP file.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">cd houses</code> to change into that directory.</li>
  <li data-marker="*">Execute <code class="highlighter-rouge">ls</code>. You should see a <code class="highlighter-rouge">characters.csv</code> file and a <code class="highlighter-rouge">students.db</code> database.</li>
</ul>

<h2 id="background">Background</h2>

<p>Hogwarts is in need of a student database. For years, the professors have been maintaing a CSV file containing all of the students’ names and houses and years. But that file didn’t make it particularly easy to get access to certain data, such as a roster of all the Ravenclaw students, or an alphabetical listing of the students enrolled at the school.</p>

<p>The challenge ahead of you is to import all of the school’s data into a SQLite database, and write a Python program to query that database to get house rosters for each of the houses of Hogwarts.</p>

<h2 id="specification">Specification</h2>

<p>In <code class="highlighter-rouge">import.py</code>, write a program that imports data from a CSV spreadsheet.</p>

<ul>
  <li data-marker="*">Your program should accept the name of a CSV file as a command-line argument.
    <ul>
      <li data-marker="*">If the incorrect number of command-line arguments are provided, your program should print an error and exit.</li>
      <li data-marker="*">You may assume that the CSV file will exist, and will have columns <code class="highlighter-rouge">name</code>, <code class="highlighter-rouge">house</code>, and <code class="highlighter-rouge">birth</code>.</li>
    </ul>
  </li>
  <li data-marker="*">For each student in the CSV file, insert the student into the <code class="highlighter-rouge">students</code> table in the <code class="highlighter-rouge">students.db</code> database.
    <ul>
      <li data-marker="*">While the CSV file provided to you has just a <code class="highlighter-rouge">name</code> column, the database has separate columns for <code class="highlighter-rouge">first</code>, <code class="highlighter-rouge">middle</code>, and <code class="highlighter-rouge">last</code> names. You’ll thus want to first parse each name and separate it into first, middle, and last names. You may assume that each person’s name field will contain either two space-separated names (a first and last name) or three space-separated names (a first, middle, and last name). For students without a middle name, you should leave their <code class="highlighter-rouge">middle</code> name field as <code class="highlighter-rouge">NULL</code> in the table.</li>
    </ul>
  </li>
</ul>

<p>In <code class="highlighter-rouge">roster.py</code>, write a program that prints a list of students for a given house in alphabetical order.</p>

<ul>
  <li data-marker="*">Your program should accept the name of a house as a command-line argument.
    <ul>
      <li data-marker="*">If the incorrect number of command-line arguments are provided, your program should print an error and exit.</li>
    </ul>
  </li>
  <li data-marker="*">Your program should query the <code class="highlighter-rouge">students</code> table in the <code class="highlighter-rouge">students.db</code> database for all of the students in the specified house.</li>
  <li data-marker="*">Your program should then print out each student’s full name and birth year (formatted as, e.g., <code class="highlighter-rouge">Harry James Potter, born 1980</code> or <code class="highlighter-rouge">Luna Lovegood, born 1981</code>).
    <ul>
      <li data-marker="*">Each student should be printed on their own line.</li>
      <li data-marker="*">Students should be ordered by last name. For students with the same last name, they should be ordered by first name.</li>
    </ul>
  </li>
</ul>

<h2 id="usage">Usage</h2>

<p>Your program should behave per the example below:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python import.py characters.csv
</code></pre></div></div>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python roster.py Gryffindor
Hermione Jean Granger, born 1979
Harry James Potter, born 1980
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
...
</code></pre></div></div>

<h2 id="hints">Hints</h2>

<ul>
  <li data-marker="*">Recall that after you’ve imported <code class="highlighter-rouge">SQL</code> from <code class="highlighter-rouge">cs50</code>, you can set up a database connection using syntax like</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">db</span> <span class="o">=</span> <span class="n">SQL</span><span class="p">(</span><span class="s">"sqlite:///students.db"</span><span class="p">)</span>
</code></pre></div></div>

<p>Then, you can use <code class="highlighter-rouge">db.execute</code> to execute SQL queries from inside of your Python script.</p>

<ul>
  <li data-marker="*">Recall that when you call <code class="highlighter-rouge">db.execute</code> and perform a <code class="highlighter-rouge">SELECT</code> query, the return value will be a <code class="highlighter-rouge">list</code> of rows that are returned, where each row is represented by a Python <code class="highlighter-rouge">dict</code>.</li>
</ul>

<h2 id="testing">Testing</h2>

<p>No <code class="highlighter-rouge">check50</code> for this problem, but be sure to test your code for each of the following.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python import.py characters.csv
$ python roster.py Gryffindor
Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980

$ python roster.py Hufflepuff
Hannah Abbott, born 1980
Susan Bones, born 1979
Cedric Diggory, born 1977
Justin Finch-Fletchley, born 1979
Ernest Macmillan, born 1980

$ python roster.py Ravenclaw
Terry Boot, born 1980
Mandy Brocklehurst, born 1979
Cho Chang, born 1979
Penelope Clearwater, born 1976
Michael Corner, born 1979
Roger Davies, born 1978
Marietta Edgecombe, born 1978
Anthony Goldstein, born 1980
Robert Hilliard, born 1974
Luna Lovegood, born 1981
Isobel MacDougal, born 1980
Padma Patil, born 1979
Lisa Turpin, born 1979

$ python roster.py Slytherin
Millicent Bulstrode, born 1979
Vincent Crabbe, born 1979
Tracey Davis, born 1980
Marcus Flint, born 1975
Gregory Goyle, born 1980
Terence Higgs, born 1979
Draco Lucius Malfoy, born 1980
Adelaide Murton, born 1982
Pansy Parkinson, born 1979
Adrian Pucey, born 1977
Blaise Zabini, born 1979
</code></pre></div></div>

<h2 id="how-to-submit">How to Submit</h2>

<p>Execute the below, logging in with your GitHub username and password when prompted. For security, you’ll see asterisks (<code class="highlighter-rouge">*</code>) instead of the actual characters in your password.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>submit50 cs50/problems/2020/x/houses
</code></pre></div></div>


</main>
