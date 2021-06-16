
import java.util.Scanner;

public class do_while1 {

	public static void main(String[] args) {
		int value = 0;
		Scanner scan = new Scanner(System.in);
		
		// 무조건 한 번은 실행하도록 하는 것
		
		do {
			//반복할 문장들
			value = scan.nextInt();//정수값을 입력받아 밸류라는 변수에 넣어준 뒤 콘솔에 출력하도록
			System.out.println("입력받은 값: "+value);
		}while(value !=10); 
			
		System.out.println("반복문 종");
			
	}

}
