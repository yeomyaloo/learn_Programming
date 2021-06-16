package 삼항연산자;

public class OperatorExam6 {
	public static void main(String[] args) {
		int b1 = (5 < 4) ? 50 : 40 ;
		//참이라면 첫 번째 값을 b1에 넣어주세요.
		//거짓이라면 두번째 값을 b1에 넣어주세요.
	
		System.out.println(b1);
	
		int b2 = 0;
	
		if(5 >
		4) {
			b2 =50;
		}else {
			b2 = 40;
		}
		System.out.println(b2);
	}
}
//삼항연산자와 if문을 변경해서 쓸 수 있다. 둘은 같은 구문임. 