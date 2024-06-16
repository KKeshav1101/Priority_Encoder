# Priority_Encoder
> A fullstack application mimicking a To-Do App but optimising it to improve productivity by predicting the relative importance of each task.<br> 
<br>
<h3>Creators</h3>
<ul>
<li><a href="https://github.com/SanjalaR">Sanjala Ramesh</a></li>
<li><a href="https://github.com/KKeshav1101">Keshav Kannan</a></li>
</ul>
<br>
<h3>Stack used</h3>
<ul>
  <li>python- pandas, tensorflow, scikit-learn</li>
  <li>html, css, javascript, bootstrap</li>
</ul>
<h3>Workflow Diagram</h3>

![Workflow Diagram (2)](https://github.com/KKeshav1101/Priority_Encoder/assets/144262889/b582816c-dfd8-4e68-8115-99259fb5fc89)

<h3>Dataset Schema</h3>
<ul>
  <li>Task_id : primary_key int </li>
  <li>Account_Name : String </li>
  <li>Current_datetime : datetime</li>
  <li>Due_datetime : datetime</li>
  <li>Brief_Description : String</li>
  <li>Task_type : Category</li>
  <li>Hours_left : hrs in decimal (derived)</li>
  <li>Weight : int in range(10)(derived)</li>
  <li>Completed : boolean</li>
</ul>
<h3>Current Status</h3>
<ul>
  <li>Built First model : for weight prediction</li>
  <li>Built basic GUI tkinter</li>
</ul>
<h3>Remaining Tasks</h3>
<ul>
  <li>Incorporate NLP into the first model</li>
  <li>Build the second model</li>
  <li>Scale up the dataset</li>
  <li>Finish the interface</li>
</ul>
<h3>Applications</h3>
<ul>
  <li>Workplace : Employer can efficiently assign tasks and ensure time is spent more appropriately on important tasks </li>
  <li>Academia : Can help with students' time management</li>
  <li>Should Increase Productivity and improve work life balance because an algorithm helps you decide where to start :) !</li>
</ul>
<h3>Scope for improvement</h3>
<ul>
  <li>The interface can be more friendly</li>
  <li>The dataset can be personalised better</li>
</ul>
<h3>Drawbacks</h3>
<ul>
  <li>Model will take time to give personalised predictions</li>
  <li>Too many input fields to enter may test your patience</li>
</ul>
