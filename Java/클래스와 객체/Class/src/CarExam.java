
public class CarExam {

	public static void main(String[] args) {
		
		//Ŭ���� - �ؾ Ʋ
		Car c1 = new Car(); //new��� ������ �ڿ� ������ ���� �����ڴ� �޸𸮿� ��ü�� ������ ��
		Car c2 = new Car();
		Car c3 = new Car();
		//�̷��� ������� ������� ��ü�� �����ϴ� c1, c2,c3�� ���������ڶ�� �Ѵ�. 
		//car ��� ��ü�� 3�� ������� ����
		
		c1.name = "�ҹ���"; //c1.name�� c1�� �����ϴ� ��ü�� ������ �ǹ� 
		c1.number = 1234;
		
		c2.name = "������";
		c2.number = 1111;
		
		System.out.println(c1.name);
		System.out.println(c1.number);
		
		System.out.println(c2.name);
		System.out.println(c2.number);
	}

}
