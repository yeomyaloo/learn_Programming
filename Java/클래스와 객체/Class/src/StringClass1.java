
public class StringClass1 {

	public static void main(String[] args) {
		// StringŬ������ �����ϴ� ��� �޼��带 ���캸��
		
		String str =new String("Hello");
		//�Ϲ������� ����� �Լ��� ����ؼ� ��ü�� �������ִ� ���ε� ��Ʈ���� ��� �� �� ����
		String str2 = "hello World";
		
		System.out.println(str2.length()); //���ڿ� ���̸� ���ؼ� ������ �����ִ� �޼��� length
		//���鵵 ���ڷ� �ν�!
		
		System.out.println(str2.concat(" love you!"));
		
		System.out.println(str2);
		//���ڿ��� �ٿ��� ��ü�� �����ϴ� ���̱� ������ �� str2�� ��ȭ���� �ʴ´�!!!
		// string �ѹ� ������� Ŭ������ �ٲ��� �ʴ´�. �Һ� Ŭ����!! 
		
		
		
		str2 = str2.concat(" love you!");
		System.out.println(str2);
		
		
		//���� �ڸ���~
		System.out.println(str2.substring(3));
		System.out.println(str2.substring(3, 7));
		
		
	}

}
