public class for4 {

	public static void main(String[] args) {
		// for ���� ��ü���� �����ʱ�ȭ, ���ǽ�, �������� �� �ٷ� ǥ���ȴ�.
		int total = 0;
		for(int i = 1; i<101; i++) {	
//			if(i%2 == 0) {
//				total = total +i;
//			}
			total = total + i;
			if (i==50) {
				break;
			}
		} 
		System.out.println(total);
	}

}