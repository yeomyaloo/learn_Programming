//�ݺ����� ����Ͽ� �迭 ����ϱ� 
public class ArrayExam2 {

	public static void main(String[] args) {
		
		
		int[] iarray = new int[100];
		iarray[0] = 1;
		iarray[1] = 2;
		System.out.println(iarray.length);
		
		//iarray.length�� �迭�� ũ�⸦ ��½�����
		for(int i = 0; i < iarray.length; i++) {
			iarray[i] = i + 1;
			}
		
		int sum = 0;	//�������� ������ ���ؼ� �ȿ��ٰ� �����ϸ� �� �ȴ�. 
		for (int i = 0; 1 < iarray.length; i++) {
			// ������ ������ - ������ ������ ������ ���� ��밡�� ������ �޶�����.
			//int sum = sum + i;�������� ������ ���ؼ� �ȿ��ٰ� �����ϸ� �� �ȴ�.
			sum = sum + iarray[i];
		}
		
		System.out.println(sum);
	}

}
