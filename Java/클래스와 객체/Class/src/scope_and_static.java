
public class scope_and_static {
	// ������ ��밡���� ������ ���´�. �� ������ ������ ��������� �Ѵ�
	int globalScope = 10; 
	static int staticVal =7;
	
	public void scopeTest(int value1) {
	//�޼��忡�� ���� �� �ִ� ����
		int localScope1 = 20;
	
		System.out.println(globalScope);
		System.out.println(localScope1);
		System.out.println(value1);
	}
	public void scopeTest2(int value2){
		int localScope2 = 20;
		
		System.out.println(globalScope);
//		System.out.println(localScope1);//���Ұ�
//		System.out.println(value1);//���Ұ�
		System.out.println(localScope2);
		System.out.println(value2);
		
	}
	
	
	public static void main(String[] args) {
		//��� Ŭ������ �ν��Ͻ�ȭ ���� ���� ä�� ����� �� ����. static�� �����Ǿ� ���� 
//		System.out.println(globalScope);
//		System.out.println(localScope);
//		System.out.println(value);
		System.out.println(staticVal);
		
		
		//static�� ������ static���� ���� ������ ����Ϸ���?
		scope_and_static v1 = new scope_and_static();
		System.out.println(v1.globalScope);
		v1.globalScope = 10;
		scope_and_static v2 = new scope_and_static();//scope_and_static�� �� Ŭ���� ��ü�� �̸�
		v2.globalScope = 20;
		System.out.println(v1.globalScope);
		System.out.println(v2.globalScope);
		
	}

}
