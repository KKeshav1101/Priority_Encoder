import java.util.*;
class Task{
	String task_desc;
	String task_type;
	Date task_date;
	Date due_date;
	int weight;
	Task(String task_desc, String task_type, Date task_date, Date due_date, int weight){
		this.task_desc=task_desc;
		this.task_type=task_type;
		this.task_date=task_date;
		this.due_date=due_date;
		this.weight=weight;
	}
	public String toString(){
		return "\nTask Description :"+task_desc+
			"\nTask Type :"+task_type+
			"\nTask Date :"+task_date+
			"\nDue Date :"+due_date+
			"\nWeight :"+weight;
	}
}
class TaskSet{
	String title;
	ArrayList<Task> tasklist;
	TaskSet(){
		title="Untitled-TaskSet";
		tasklist=new ArrayList<Task>();
	}
	TaskSet(String title){
		this.title=title;
	}
	void display(){
		for(Task ts:tasklist){
			System.out.println(""+ts);
		}
	}
}
