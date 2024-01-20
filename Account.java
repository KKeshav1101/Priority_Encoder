class Account{
	String name;
	int age;
	String gender;
	ArrayList<TaskSet> list = new ArrayList<TaskSet>();		

	public Account(String name, int age, String gender){
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
	
	public String toString(){
		return "User Details\nName: "+name+"\nAge: "+age+"\nGender: "+gender;
	}
	public void addTaskSet(TaskSet ts){
		list.add(ts);
	}
	public void removeTaskSet(TaskSet ts){
		list.remove(ts);
	}
}
