# Ativdade ponderada 2 de programção

## 1. Introdução

O projeto atualmente contém arquivos : este readme, um arquivo com a estrutura de dados pilha e código que cria um nodo do ros2 que controla o robô. Esse código foi feito para ser usado junto empty_world.launch.py que é um package do ros2 que pode ser executado com o comando:

```
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

O código do robô pode ser executado com o comando:

```
python3 robot_mover.py
```

## 2. Estrutura de dados

A estrutura de dados utilizada foi a pilha, que é uma estrutura de dados linear que segue o princípio LIFO (Last In First Out), ou seja, o último elemento a entrar é o primeiro a sair. A pilha é uma estrutura de dados que pode ser implementada de diversas formas, como por exemplo, com um vetor ou com uma lista encadeada. Nesse projeto foi utilizada uma lista encadeada, pois a quantidade de elementos que a pilha pode conter é variável e não é necessário alocar um espaço de memória fixo para a pilha. A pilha é uma estrutura de dados que pode ser utilizada em diversas aplicações, como por exemplo, na implementação de um sistema de navegação de um robô, onde a pilha pode ser utilizada para armazenar os pontos de navegação que o robô deve percorrer.

## 3. Código

O código do robô foi feito em python3 e utiliza a biblioteca rclpy do ros2 para criar um nodo que controla o robô. O código do robô cria uma pilha e insere nela os pontos de navegação que o robô deve percorrer. O robô percorre os pontos de navegação que estão na pilha e quando chega no último ponto, ele volta para o primeiro ponto. O robô primeiramente checa se ele esta perto do ponto da pilha atual, se não estiver ele checa se está na direção do ponto, se não estiver ele gira até ficar na direção do ponto e depois anda em linha reta até chegar perto do ponto. Quando o robô chega perto do ponto ele o remove da pilha e vai para o próximo ponto. Quando o robô chega no último ponto da pilha ele volta para o primeiro ponto da pilha e repete o processo. Olhamos o topico odometry para saber a posição e ângulo do robô e o tópico cmd_vel para controlar o robô.

## 4. Video
Dentro do projeto existe um arquivo de vídeo chamado video demonstrando o funcionamento do projeto
