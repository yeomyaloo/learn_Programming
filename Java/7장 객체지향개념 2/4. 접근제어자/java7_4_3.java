package javaStandard;

final class FinalTest{
	
	final int MAX_SIZE = 10; //��� ����
	
	final void getMaxSize() {
		final int LV = MAX_SIZE; // �������� ---> �޼ҵ� �ȿ� �����ϱ�
		return MAX_SIZE;
	}	
}

clsaa Child extends FinalTest{
	void getMaxSize() {} // ����, �������̵� �Ұ�
}