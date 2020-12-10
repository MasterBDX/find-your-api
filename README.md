# find-your-api
<p><span style="font-size:26px">About Find Your API</span></p>

<p><span style="font-size:18px">This site provide you a free fake online rest api to make your tests, be free to check our API guides <a href="http://127.0.0.1:8000/guides/">here</a> .</span></p>

<hr />
<h2><span style="font-size:22px">API Resources List :</span></h2>

<ul>
	<li><span style="font-size:18px">Users API</span></li>
	<li><span style="font-size:18px">Posts API</span></li>
	<li><span style="font-size:18px">Comments API</span></li>
	<li><span style="font-size:18px">Blog API</span></li>
	<li><span style="font-size:14px">soon more resources will be added ...</span></li>
</ul>

<hr />
<p><span style="font-size:22px">All HTTP methods are supported.</span></p>

<p><span style="font-size:18px"><span style="color:#f1c40f">GET</span> | <span style="color:#2ecc71">POST</span> | <span style="color:#3498db">PUT</span> | <span style="color:#2980b9">PATCH</span> | <span style="color:#c0392b">DELETE </span></span></p>

<hr />
<p><span style="font-size:18px">You can make get requests , fetch data dirctly from our website and copy it from section below .</span></p>

<p><span style="font-size:16px"><strong>Important Notes :</strong></span></p>

<p><span style="font-size:16px"><strong>1- You can make 200 request per hour <span class="marker">( 200 / hour )</span> otherwise your request will be rejected.</strong></span></p>

<p><span style="font-size:16px"><strong>2- All Requests we provide are fake ,will not be updated on server .</strong></span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px">I hope you find my website helpful : )&nbsp; </span></p>

<p><strong><em>MBDX</em></strong></p>


Clone This Project (Make Sure You Have Git Installed)

make your Virtualenv.

Install Dependencies :

``` pip install -r requirements.txt ```

Set Database (Make Sure you are in directory same as manage.py)

``` python manage.py makemigrations ```

``` python manage.py migrate ```

Create SuperUser :

``` python manage.py createsuperuser ```

After all these steps , you can start testing and developing this project. That's it! Happy Coding!
