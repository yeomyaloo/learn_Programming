
public class method2 {
	
	
	public static void main(String[] args) {
		// class�� ���� �޼ҵ带 ����ϱ� ���ؼ��� ��ü�� ������ ����� �� �ִ�.
		
		method1 myclass = new method1();
		// ����� Ŭ������ / ���� �� Ŭ�������� �ٽ� �� �̸� = new ����� Ŭ������();
		
		myclass.method1_1();
		myclass.method1_2(10);
		
		int value = myclass.method1_3();
		System.out.println("m3�� ������ ��" + value);
		
		myclass.method1_4(5, 10);
		
		int value2 = myclass.method1_5(55);
		System.out.println("m5�� ������ ��" + value2);
				
	}
}
