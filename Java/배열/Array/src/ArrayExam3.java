
public class ArrayExam3 {
//2���� �迭 =�迭�� �迭
	public static void main(String[] args) {
		int [][] array4 = new int[3][4]; //3�� 4��
		//array4 = ������ �迭�� ����Ű�� ���� 
		array4[0][0] = 10; // array4[0] =10�� ��쿣 �����ϴ� �Ϳ� ���� �ο��ϴ� ���̶� �� ��
		
		int [][] array5= new int[3][];
		array5[0] = new int[1]; //2. ���� �������� ũ�⸦ �������־�� �Ѵ�. 
		
		//1. array5[0][0] = 10; �̰͵� ���� ���� ������ ��� ���� �� 
		array5[0][0] = 10;
		
		// 2���� �迭�� ����� ���ÿ� �ʱ�ȭ �ϴ� ���
		int[][] array6 = {{1},{1,2},{1,2,3}};
		
	
		System.out.println(array6[0][0]);
	
		
		
			
	}

}
