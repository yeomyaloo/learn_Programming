public class for4 {

	public static void main(String[] args) {
		// for 구문 자체에서 변수초기화, 조건식, 증감식이 한 줄로 표현된다.
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