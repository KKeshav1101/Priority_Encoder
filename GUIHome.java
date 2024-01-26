import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

class GUIHome{
	JFrame jf;
	JPanel jp;
	JButton accedit;
	JMenu user, view;
	JMenuBar jmb;
	JLabel acclabel;
	JButton addbtn;
	
	GUIHome(){
		jf = new JFrame("Priority Encoder");
		jf.setSize(750, 600);
		jf.setLayout(new GridLayout(2,1,20,10));
		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		jmb = new JMenuBar();
		user = new JMenu("User");
		JMenuItem viewacc = new JMenuItem("View Account");
		JMenuItem editacc = new JMenuItem("Edit Account");
		user.add(viewacc);
		user.add(editacc);
		jmb.add(user);
		view = new JMenu("View");
		JMenuItem theme = new JMenuItem("Theme");
		JMenuItem font = new JMenuItem("Font");
		view.add(theme);
		view.add(font);
		jmb.add(view);
		jf.setJMenuBar(jmb);

		jp=new JPanel();
		addbtn=new JButton("Add TaskSet");
		addbtn.setForeground(Color.white);
		addbtn.setBackground(new Color(51,153,255));
		jp.add(addbtn);
		jf.add(jp);

		addbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent ae){
				new TaskSetAdd();
			}
		});
		
		jf.repaint();
		jf.setVisible(true);
	}

	public static void main(String args[]){
		new GUIHome();
	}
}

class TaskSetAdd{
	JFrame jf;
	JButton addbtn,save;
	JLabel dummy=new JLabel("");
	JTextField title;
	JTextField tdesc,weight,ddate,tdate;
	JComboBox<String> type;
	JScrollPane jsp; 
	TaskSetAdd(){
		jf=new JFrame("Add Task Set");
		jf.setVisible(true);
		jf.setLayout(new FlowLayout(FlowLayout.LEFT));
		jf.setSize(600,600);

		//jsp=new JScrollPane();
	
		title=new JTextField("Title",15);
		jf.add(title);

		dummy.setPreferredSize(new Dimension(3000,0));
		jf.add(dummy);

		addbtn=new JButton("Add Task");
		jf.add(addbtn);

		jf.add(dummy);

		String arr[]={"School","Club","Work","Personal","Other"};		
		
		addbtn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent ae){
				tdesc=new JTextField("Description");
				jf.add(tdesc);
				type=new JComboBox<String>(arr);
				jf.add(type);
				tdate=new JTextField("Task Date");
				jf.add(tdate);
				ddate=new JTextField("Due Date");
				jf.add(ddate);
				weight=new JTextField("Wt. on a scale of 10");
				jf.add(weight);
				save=new JButton("Save Task");
				jf.add(save);
				jf.add(dummy);
				jf.revalidate();
			}
		});
				
		jf.repaint();
		jf.revalidate();
	}
}

