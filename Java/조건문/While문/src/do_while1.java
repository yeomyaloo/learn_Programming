
import java.util.Scanner;

public class do_while1 {

	public static void main(String[] args) {
		int value = 0;
		Scanner scan = new Scanner(System.in);
		
		// ������ �� ���� �����ϵ��� �ϴ� ��
		
		do {
			//�ݺ��� �����
			value = scan.nextInt();//�������� �Է¹޾� ������ ������ �־��� �� �ֿܼ� ����ϵ���
			System.out.println("�Է¹��� ��: "+value);
		}while(value !=10); 
			
		System.out.println("�ݺ��� ��");
			
	}

}
