
public class StringExam {

	public static void main(String[] args) {
		// String�� new��� �����ڰ� ��� �ν��Ͻ��� ����� �� �� �ִ�. 
		String str1 = "Hello"; //��������� ������� hello
		String str2 = "Hello"; // str2�� �̹� ������� ������� hello�� �ֱ� ������ str1�� ���� �ν��Ͻ��� �����Ѵ�.
		
		String str3 = new String("Hello"); //��������� �ִ� ���� �ƴ� ���� �ν���Ʈ�� hip������ ���� �װ��� ����
		String str4 = new String("Hello"); // str3 str4�� ���������� �ٸ� �ν��Ͻ��� ���� ���� �ٸ� �ν��Ͻ��� ����Ų��. 
		
		if(str1 == str2) 
			System.out.println("str1 str2�� ���� ���۷����Դϴ�.");
		if(str3 == str4)
			System.out.println("str3 str4�� ���� ���۷����Դϴ�.");
		else
			System.out.println("str3 str4�� �ٸ� ���۷����Դϴ�.");
		
		//�� �� ������ Ŭ������ ��ȭ���� �ʴ´�. - string�� ��Ư�� ��
		
		System.out.println(str1);
		System.out.println(str1.substring(3)); //3�� �ε����� �߶� �����ּ���
		System.out.println(str1); //�ѹ� ������� Ŭ���� ���� ��ȭ���� �ʴ´�.!! 	
	}

}
