# 1 тур
## 1
Дано рівнобедрений трикутник $ABC (AB = AC)$. Позначимо через $M$ середину сторони $BC$. Нехай $X$ – деяка точка на меншій з дуг $MA$ описаного навколо трикутника $ABM$ кола. Точка $T$, що лежить всередині кута $BMA$, така, що $\angle TMX = 90^\circ$ та $TX = BX$. Доведіть, що різниця $\angle MTB - \angle CTM$ не залежить від положення точки $X$.
<details><summary>Розв’язання 1</summary>

Нехай точка $N$ – середина сегмента $BT$. Рівнобедрений трикутник $BXT$ симетричний відносно прямої $XN$, тому $\angle TNX = 90^\circ$ та $\angle BXN = \angle NXT$. Більше того, в трикутнику $BCT$, пряма $MN$ – середня лінія, отже вона паралельна $CT$, тому $\angle CTM = \angle NMT$.

Завдяки прямим кутам, точки $M$ та $N$ лежать на колі з діаметром $XT$. Звідси $\angle MTB = \angle MTN = \angle MXN$ та $\angle CTM = \angle NMT = \angle NXT = \angle BXN$. Тобто $\angle MTB - \angle CTM = \angle MXN - \angle BXN = \angle MXB = \angle MAB$, останній не залежить від положення точки $X$.
</details>
<details><summary>Розв’язання 2</summary>

Нехай точка $S$ – це точка, симетрична точні $T$ відносно $M$. Тоді $XM$ є серединним перпендикуляром до $TS$, тому $XB = XT = XS$, і точка $X$ є центром описаного кола трикутника $BST$. Більше того, $\angle BSM = \angle CTM$ так як вони симетричні відносно точки $M$. Тоді $\angle MTB - \angle CTM = \angle STB - \angle BST =\frac{1}{2}(\angle SXB - \angle BXT)$. Зауважимо що $\angle SXB = \angle SXT - \angle BXT = 2\angle MXT - \angle BXT$, тому $\angle MTB - \angle CTM = \frac{1}{2}(2\angle MXT - 2\angle BXT) = \angle MXB = \angle MAB$, що не залежить від положення точки $X$.
</details>

## 2
У рядок записані символи – цифри від 0 до 9 та українські букви (їх 33). Деякі символи можуть повторюватися. При цьому у рядку немає таких двох різних цифр $n_i$ та $n_j$, що $n_i > n_j$ та $n_i$ знаходиться у рядку лівіше за $n_j$. Також немає таких двох різних букв $l_i$ та $l_j$, що $l_i$ зустрічається у алфавіті пізніше за $l_j$ і при цьому $l_i$ знаходиться у рядку лівіше за $l_j$. Також немає двох однакових символів, які ідуть підряд або через один символ. Яка найбільша кількість символів (цифр та букв разом) може бути у такому рядку?
<details><summary>Відповідь</summary>
73
<details><summary>Розв’язання</summary>

Розглянемо випадок, коли є деякий символ $s_j$, що зустрічається у рядку не вперше. Нехай $s_i$ – найправіший символ, що співпадає з $s_j$ і стоїть перед $s_j$. Тоді, за умовою, між $s_i$ та $s_j$ є відрізок не менше, ніж з 2 символів. При цьому всі символи цього відрізка мають інший тип, ніж $s_j$: якщо $s_j$ – цифра, то між $s_i$ та $s_j$ будуть тільки букви, і навпаки. Дійсно, якщо між $s_i$ та $s_j$ буде символ $s_k$ того ж типу, то він має задовольняти $s_i \leq s_k \leq s_j$, якщо $s_j$ – цифра, або $ord(s_i) \leq ord(s_k) \leq ord(s_j)$, якщо $s_j$ – буква. ($ord(l)$ – це порядок букви $l$ у алфавіті.) Тобто, має бути $s_k = s_j$, але за вибором $s_i$ такого бути не може.

Назвемо відрізок рядка *стандартним*, якщо він містить символи лише одного типу (тільки цифри або букви), і при цьому символи, що межують з цим відрізком, мають інший тип. Відрізок назвемо *довгим*, якщо він містить більше 1 символу. Тоді кожен символ, що зустрічається у рядку не вперше, відповідає деякому довгому стандартному відрізку, який межує з символом своїм правим кінцем.

Нехай у рядку є $a$ довгих стандартних відрізків з цифрами, і $b$ довгих стандартних відрізків з буквами. Тоді у рядку – не більше $(10 + b)$ цифр і не більше $(33 + a)$ букв. Дійсно, кожна цифра, що зустрічається не вперше, відповідає одному з $b$ довгих стандартних буквених відрізків; а цифр, що зустрічаються вперше, може бути максимум 10. Аналогічно – для букв.

Тепер помітимо, що ліва і права цифри довгого стандартного відрізка відрізняються між собою. Інакше усередині цього стандартного відрізка були би і букви, а цього не може бути з означення стандартності. Якщо проходити рядок зліва направо, то при проходженні кожного довгого стандартного відрізка остання з розглянутих цифр збільшується принаймні на 1. Отже, у рядку – не більше 9 довгих стандартних цифрових відрізків. Тому у ньому не більше $33+ 9 = 42$ букв. З цих букв можна зробити не більше $\frac{42}{2} = 21$ довгого стандартного відрізка. Отже, у рядку не більше $10 + 21= 31$ цифр. Тому разом буде не більше $42 + 31= 73$ символів.

Побудуємо рядок з 73 символів: $$0аб01бв12вг23гґ34ґд45де56еє67єж78жз89зи9ії9йк9лм9но9пр9ст9уф9хц9чш9щю9яь9$$ (Легко вказати закономірність, але для кращої зрозумілості приклад наведено повністю.)
</details></details>

## 3
Для додатних чисел $a$, $b$, $c$, $d$ довести нерівність:
```math
(a+b)(b+c)(c+d)(d+a)(1+\sqrt[4]{abcd}) \geq 16abcd(1+a)(1+b)(1+c)(1+d).
```
<details><summary>Розв’язання</summary>

**Лема.** Для невід’ємних $x$, $y$ справджується нерівність: $\frac{x+y}{(1+x)(1+y)} \geq \frac{2\sqrt{xy}}{(1+\sqrt{xy})^2}$.
<details><summary>Доведення</summary>

Позначимо $t = x + y$. Тоді твердження леми випливає з монотонності функції $f(t) = \frac{t}{1+t+xt}$ та нерівності $t = x + y \geq 2\sqrt{xy}$. Лема доведена. $\blacksquare$
</details>

Застосуємо лему до чисел $(a,b)$ і $(c,d)$: $\frac{a+b}{(1+a)(1+b)} \geq \frac{2\sqrt{ab}}{(1+\sqrt{ab})^2}$, $\frac{c+d}{(1+c)(1+d)} \geq \frac{2\sqrt{cd}}{(1+\sqrt{cd})^2}$, то
```math
\frac{a+b}{(1+a)(1+b)} \frac{c+d}{(1+c)(1+d)} \geq \frac{2\sqrt{ab}}{(1+\sqrt{ab})^2} \frac{2\sqrt{cd}}{(1+\sqrt{cd})^2}. \tag{1}
```
Тепер її застосуємо до чисел $(\sqrt{ab},\sqrt{cd})$: $\frac{\sqrt{ab}+\sqrt{cd}}{(1+\sqrt{ab})(1+\sqrt{cd})} \geq \frac{2\sqrt{\sqrt{ab}\cdot\sqrt{cd}}}{(1+\sqrt{\sqrt{ab}\cdot\sqrt{cd}})^2}$, а тому, оскільки $(b+c)(a+d) \geq (\sqrt{ab}+\sqrt{cd})^2$, то $(\sqrt{ab}+\sqrt{cd})^2 \geq \frac{(1+\sqrt{ab})^2 (1+\sqrt{cd})^2 4\sqrt{abcd}}{(1+\sqrt[4]{abcd})^4}$, тому
```math
(b+c)(a+d) \geq \frac{(1+\sqrt{ab})^2 (1+\sqrt{cd})^2 4\sqrt{abcd}}{(1+4\sqrt{abcd})^4}. \tag{2}
```
Тепер перемножимо нерівності (1) і (2) одержимо:
```math
\frac{(a+b)(b+c)(c+d)(d+a)}{(1+a)(1+b)(1+c)(1+d)} \geq \frac{2\sqrt{ab}}{(1+\sqrt{ab})^2} \frac{2\sqrt{cd}}{(1+\sqrt{cd})^2} \frac{(1+\sqrt{ab})^2 (1+\sqrt{cd})^2 4\sqrt{abcd}}{(1+\sqrt[4]{abcd})^4},
```
після простих перетворень та скорочень одержимо шукане.
</details>

# 2 тур
## 4
Кола $w_1$, $w_2$ дотикаються внутрішнім чином в точці $P$. На їх спільній дотичній по різні боки від точки $P$ обрані точки $A$ і $B$. Нехай $C$ – точка перетину дотичних, що проведені з точки $A$ до кола $w_1$, і з точки $B$ до кола $w_2$, точка $D$ – точка перетину дотичних, що проведені з точки $B$ до кола $w_1$, і з точки $A$ до кола $w_2$. Довести, що $CA+CB = DA+DB$.
<details><summary>Розв’язання</summary>

Позначимо точки перетину відповідних прямих таким чином $L = AC \cap BD$, $K = AD \cap BC$. Очевидно, що $BL + AK = AL + BK$. Покажемо, що чотирикутник $LDKC$ – описаний. Побудуємо коло, яке вписане в $\triangle BDK$ і проведемо дотичну $AC_1$ до цього кола, яка відмінна від $AK$ ($C_1 \in BK$). Нехай $L_1 = AC_1 \cap BD$, $X$, $Y$, $Z$, $T$ – точки дотику побудованого кола до прямих $BD$, $DK$, $KB$, $AC_1$ відповідно. Тоді $AL_1 + BK = AT −TL_1 + BZ + ZK = KY + BX − L_1X + AY = AK + BL_1$, або $AL_1 − BL_1 = AK − BK = AL − BL$. Якщо, наприклад, $BL > BL_1$, то $AL_1 + BL = BL_1 + LL_1 + AL_1 > BL_1 + AL$ - суперечність. Таким чином $L = L_1$, тому $LDKC$ – описаний, звідки $DL + CK = LC + KD$, або $(LC + KD) + (AL + BK) = (LD + CK) + (BL + AK)$, звідки $AC + BC = AD + BD$, що й треба було довести.
</details>

## 5
Знайти усі функції $f : \mathbb{R}^+ \to \mathbb{R}^+$ такі, що $f(x + f(y)) = f(x + y) + f(y)$ для усіх $x, y \in \mathbb{R}^+$.
<details><summary>Відповідь</summary>

$f(x) = 2x$
<details><summary>Розв’язання</summary>

Доведемо спочатку, що $f(y) > y$ для всіх $y \in \mathbb{R}^+$. З умови випливає, що $f(x + f(y)) > f(x + y)$, а з цієї нерівності отримуємо, що $f(y) \neq y$. Припустимо, що для деякого $y$ виконується $f(y) < y$. Підставимо у рівняння $x = y − f(y)$. Отримуємо $f(y) = f((y − f(y)) + f(y)) = f((y − f(y)) + y) + f(y) > f(y)$, протиріччя. Тому $f(y) > y$ для всіх $y \in \mathbb{R}^+$.

Для довільного $x \in \mathbb{R}^+$ покладемо $g(x) = f(x)− x$, тоді $f(x) = g(x)+ x$ і, як було щойно доведено, $g(x) > 0$. Перетворимо рівняння $f(x + f(y)) = f(x + y)+ f(y)$ для функції $g(x)$, при цьому покладемо $t = x + y$: $f(t + g(y)) = f(t)+ f(y)$, $g(t + g(y))+ t + g(y) = (g(t)+ t)+ (g(y)+ y)$, тобто для всіх $t > y > 0$
```math
g(t + g(y)) = g(t)+ y. \tag{1}
```

Доведемо ін’єктивність функції $g(x)$. Припустимо, що $g(y_1) = g(y_2)$ для деяких $y_1, y_2 \in \mathbb{R}^+$. Тоді з (1) маємо $g(t) + y_1 = g(t + g(y_1)) = g(t + g(y_2)) = g(t + y_2)$ для усіх $t > \max\{y_1, y_2\}$. Отже, $g(y_1) = g(y_2)$ можливе лише при $y_1 = y_2$.

Нехай $u$, $v$ – довільні дійсні числа та $t > u + v$. Застосуємо (1) тричі та отримаємо $g(t + g(u)+ g(v)) = g(t + g(u))+ v = g(t)+ u + v = g(t + g(u + v))$. Завдяки ін’єктивності функції $g(x)$ отримуємо $t + g(u)+ g(v) = t + u + v$, отже
```math
g(u)+ g(v) = u + v. \tag{2}
```
А так як функція $g(x)$ додатна, то з (2) випливає, що вона зростає. Доведемо, що $g(x) = x$. Поєднуємо (1) та (2), знаходимо $g(t)+ y = g(t + g(y)) = g(t)+ g(g(y))$, а тому $g(g(y)) = y$.

Припустимо, що існує таке $x \in \mathbb{R}^+$, що $g(x) \neq x$. Завдяки монотонності функції $g(x)$, якщо $x > g(x)$, то $g(x) > g(g(x)) = x$, – протиріччя. Аналогічно для випадку $x < g(x)$, а тому $g(x) = x$.

Ми довели, що $g(x) = x$, а отже $f(x) = g(x)+ x = 2x$ для всіх $x \in \mathbb{R}^+$, перевірка показує, що ця функція задовольняє умові.
</details></details>

## 6
Довести, що існує нескінченно багато пар різних натуральних чисел $(a,b)$ відмінних від 1, для яких виконується умова:
```math
(b^b + a) \vdots (a^a+b).
```
<details><summary>Розв’язання</summary>

Нехай $a$ – фіксоване, будемо шукати $b^n$ серед таких, що $a^a + b = a^{m+1}$, тобто $b = a^m - a^a + 1$. Тоді $b^b + a = ((a^m + 1) - a^a)^b + a \equiv (-a^a)^b + a \mod(a^a+b)$. Оскільки $b$ - непарне, то $(-a^a)^b + a = -a^{ab} + a = -a(a^{ab-1}-1)$. Таким чином нам достатньо, щоб $(a^{ab-1}-1) \mathop{\raisebox{-2pt}{\vdots}} (a^m+1)$, а для цього достатньо, щоб $(2m) | (ab - 1) = a(a^m - a^a + 1) - 1 = (a^{m+1} - 1) - (a^a - 1)a$. Тепер знову будемо шукати $(2m)$ серед дільників $(a^k - 1)$. Якщо $k | (m + 1)$ і $k | a$, то $(2m) | (a^k - 1) | ((a^{m+1} - 1) - (a^a - 1))$. Виберемо $k = 3$ $a^3-1=(a-1)(a^2+a-1)$, нехай $2m=2q(a^2+a+1)$, де $(2q)|a-1$. Тоді $(2m) | (a^3 - 1)$, ще треба, щоб виконувались умови $3 | (m + 1) = q(a^2 + a + 1)$ та $3 | a$. Тобто $3|a$ і $3|(q+1)$ - виберемо $q=2$, тоді $m = 2(a^2 + a + 1)$ і, якщо $3 | a$ та $4 | (a - 1)$, то пара $(a, a^m - a^a + 1)$ задовольняє умови.
</details>

## 7
На площині є граф $\Gamma_0$ з вершинами $A_1, A_2, \ldots, A_n$. Граф $\Gamma_{m+1}$ будується таким чином – у графі $\Gamma_m$ витираємо усі ребра, а нові ребра будуються за правилом: дві різні вершин $A_i$ і $A_j$ з’єднуються ребром тоді і тільки тоді, коли існує відмінна від них третя вершина $A_k$ така, що $A_k$ була одночасно зв’язана з $A_i$ і $A_j$. Довести, що нескінченна послідовність $(\Gamma_m, m \in \mathbb{N})$ починаючи з деякого номера періодична з періодом $T \leq 2^n$.
<details><summary>Розв’язання</summary>

Покажемо індукцією по $n$, що усі $\Gamma_k$, починаючи з деякого місця, будуть утворювати декілька компонент зв’язності (КЗ), для кожної з яких можливі три варіанти – 1) ізольована точка; 2) цикл непарної довжини, не меншої 5; 3) повний граф не менше ніж на 3–х вершинах.

База очевидна.

Нехай це справджується для усіх $x < N$, покажемо твердження для $N$. Якщо для деякого $k$ $\Gamma_k$ перестав бути зв’язним, то все випливає з припущення індукції до одержаних КЗ. Нехай усі $\Gamma_k$ зв’язні $\forall k \in N$. Позначимо $\forall k \in N$ через $\Delta_k$ кількість вершин у найбільшому повному підграфі.

Якщо у графі $\Gamma_0$ степені усіх вершин менше або дорівнює 2, і, оскільки він зв’язний, то це або цикл, що проходить через усі вершини графа, або цикл без одного ребра. Для циклу з непарною кількістю вершин усі зрозуміло. Це буде знову цикл, усього таких різних циклів не більше $n^2$. Для циклу з парною кількістю вершин вже $\Gamma_1$ – незв’язний, що суперечить припущенню. Так само в разі циклу без одного ребра $\Gamma_1$ – незв’язний.

Інакше у графі $\Gamma_0$ є вершина степені не менше 3, тобто деяка вершина $A_0$ з’єднана з $A_1$, $A_2$, $A_3$, то $\Delta_1 \geq 3$, оскільки усі ці вершини будуть з’єднані в $\Gamma_1$. Якщо є повний підграф $F$ степені $\Delta_k$, то він залишається у кожному наступному графі. Або він повністю співпадає з $\Gamma_k$, тоді все доведено. Або, оскільки він зв’язний, є ребро $A_\alpha A_\beta$, яке йде з $A_\alpha \in F$ в $A_\beta \in \bar F$. Але тоді вершина $A_\beta$ буде зв’язана з усіма вершинами $F$ у графі $\Gamma_{k +1}$, тобто наступний граф буде містити повний підграф з кількістю вершин принаймні на 1 більшу від $\Gamma_k$. Але тоді з умов $\Delta_{k +1} \geq \Delta_k$ і $\Delta_1 \geq 3$, то $\Delta_N > N$ – суперечність.

Таким чином $\Gamma_0$ складається з декількох КЗ. Далі просто індукцією довести потрібну оцінку. Період $\Gamma_k$ – НСК періодів КЗ, звідки легко одержати потрібну оцінку:
```math
[T(S_1),\ldots, T(S_r)] \leq T(S_1) \times \ldots \times T(S_r) \leq 2^{\alpha_1} \ldots 2^{\alpha_r} \leq 2^N.
```
</details>

## 8
Розглянемо функції $f : \mathbb{N} \to \mathbb{N}$, які задовольняють умову $f(m+n) \geq f(m) + f(f(n)) - 1$ для усіх $m, n \in \mathbb{N}$. Знайдіть усі можливі значення $f(2008)$.
<details><summary>Відповідь</summary>

$1, 2, \ldots, 2009$
<details><summary>Розв’язання</summary>

Нехай деяка функція $f$ задовольняє умові. Для довільних натуральних чисел $m > n$ маємо $f (m) = f (n + (m − n)) \geq f (n) + f (f (m − n)) - 1 \geq f (n)$, отже функція $f$ – неспадна.

Очевидно, що функція $f \equiv 1$ задовольняє умові. Щоб знайти інші розв’язки, припустимо, що $f \not\equiv 1$ та розглянемо найменше значення $a \in \mathbb{N}$, для якого $f (a) > 1$. Тоді $f (b) \geq f (a) > 1$ для всіх натуральних чисел $b \geq a$. Припустимо, що для деякого натурального $n$ виконується $f (n) > n$. Тоді маємо $f (f (n)) = f ((f (n)− n) + n) \geq f (f (n)− n) + f (f (n)) − 1$, тому $f (f (n)− n) \leq 1$, а значить $f (n)− n < a$. Тоді існує найбільше значення виразу $f (n)− n$. Позначимо його через $c$, і нехай $f (k)− k = c \geq 1$. Застосувавши монотонність та умову задачі, знайдемо $2k + c \geq f (2k) = f (k + k) \geq f (k) + f (f (k)) − 1 \geq f (k) + f (k) − 1 = 2(k + c) − 1 = 2k + (2c − 1)$, отже $c \leq 1$ та $f (n) \leq n + 1$ для всіх натуральних $n$. Зокрема, $f (2008) \leq 2009$.

Далі ми наведемо сім’ю прикладів, які показують, що всі значення від 1 до 2009 можливі. Нехай $f_j(n) = \max\{1, n + j − 2008\}$ для $j=1,2,\ldots,2008$; $f_{2009}(n) = \begin{cases} n, &2008 \not | n \\ n+1, &2008|n \end{cases}$

Ми покажемо що ці функції задовольняють умову задачі. Зрозуміло, що для кожної з них $f_j (2008) = j$. Для перевірки умови
```math
f (m + n) \geq f (m) + f (f (n)) − 1 \tag{1}
```
для функції $f_j (j \leq 2008)$, відмітимо спочатку, що $f_j$ – неспадна та $f_j(n) \leq n$, тому $f_j(f_j(n)) \leq f_j(n) \leq n$ для всіх $n \in \mathbb{N}$. Якщо $f_j(m) = 1$, то нерівність (1) виконується, так як $f_j(m + n) \geq f_j(n) \geq f_j(f_j(n)) = f_j(m) + f_j(f_j(n))−1$. В іншому випадку $f_j(m) + f_j(f_j(n)) − 1 \leq m + j − 2008 + n = (m+n) + j − 2008 = f_j(m + n)$.

У випадку $j = 2009$, зрозуміло, що $n + 1 \geq f_{2009}(n) \geq n$ для всіх натуральних $n$. Більше того, $n + 1 \geq f_{2009}(f_{2009}(n))$. Якщо $f_{2009}(n) = n$, то це зрозуміло; інакше $f_{2009}(n) = n + 1$, завдяки чому 2008 не ділиться на $n + 1$, а тому $n+1=f_{2009}(n+1) = f_{2009}(f_{2009}(n))$.

Отже, якщо $2008 | m + n$, то $f_{2009} (m + n) = m + n + 1 = (m + 1) + (n + 1) − 1 \geq f_{2009} (m) + f_{2009} (f_{2009} (n)) − 1$. Якщо ж $2008 \not | m + n$, то $2008 \not | m$ або $2008 \not | n$. В першому випадку маємо $f_{2009}(m) = m$, в другому – $f_{2009}(f_{2009}(n)) = f_{2009}(n) = n$, що дає $f_{2009}(m) + f_{2009}(f_{2009}(n)) − 1 \leq (m + n + 1) − 1 = f_{2009}(m + n)$.

**_Зауваження._** Можливі інші приклади функцій. Нижче наведено дві конструкції прикладів для $j \leq 2008$ (без доведення):
$$g_j(n) =
\begin{cases}
1, &n<2008 \\
j, &n = 2008\\
n, &n>2008
\end{cases},
$$
$$h_j(n) = \max\left\{1, \lfloor \frac{jn}{2008} \rfloor\right\}$$
</details></details>

## 9
Заданий $\triangle ABC$ і точка $D$ всередині трикутника. Позначимо точки перетину прямих $A_0 = AD \cap BC$, $B_0 = BD \cap AC$, $C_0 = CD \cap AB$. Нехай $A_1$, $B_1$, $C_1$, $A_2$, $B_2$, $C_2$ – середини відрізків $BC$, $AC$, $AB$, $AD$, $BD$, $CD$ відповідно. Через точку $B_0$ проведено прямі, які паралельні $A_1A_2$ та $C_1C_2$, які перетинають пряму $B_1B_2$ в точках $A_3$ і $C_3$ відповідно. Довести, що $\frac{A_3B_1}{A_3B_2} = \frac{C_3B_1}{C_3B_2}$.
<details><summary>Розв’язання</summary>

Зобразимо відповідні елементи. Відкладемо відрізок $A'B'$, відмітимо на ньому точку $C_0'$ таким чином, щоб виконувалась рівність $\frac{A'C_0}{B'C_0'} = \frac{AC_0}{BC_0}$, а на відрізку $B'C_0'$ відмітимо точку $C_1'$ так, щоб $\frac{B'C_1'}{C_1C_0'} = \frac{BA_0}{CA_0}$. Нехай $A_0'$ – одна з точок перетину кола з діаметром $A'B'$ та перпендикуляра до цього діаметру в точці $C_1'$, $C'$ – точка перетину прямої $'A_0'$ з перпендикуляром до $A'B'$ в точці $C_0'$ , $D' = A'A_0' \cap C'C_0'$. Очевидно, що $D'$ – ортоцентр $\triangle A'B'C'$.

Переведемо афінним перетворенням $\triangle ABC \rightarrow \triangle A'B'C'$, тоді $A_0 \rightarrow A_0'$, $B_0 \rightarrow B_0'$, $C_0 \rightarrow C_0'$, $D \rightarrow D'$, оскільки афінні перетворення зберігають відношення паралельних відрізків. Отже ми звели задачу до випадку, коли $D$ – ортоцентр $\triangle ABC$.

Зробимо гомотетію з центром в точці $D$ і коефіцієнтом 2, тоді $A_2$, $B_2$, $C_2$ перейдуть у $A$, $B$, $C$ відповідно, точки $A_1$, $B_1$, $C_1$ в діаметрально протилежні до точок $A$, $B$, $C$, а також $B_0 \rightarrow D_0$, $A_3 \rightarrow D_2$, $C_3 \rightarrow D_3$, причому $D_3D_0\parallel CO$, $D_2D_0\parallel AO$, $D_1D_0 \perp AC \perp BD$ $\implies \angle D_1D_0D_2 = \angle OAC = \angle OCA = \angle D_1D_0D_3$, отже $D_0D_1$ – бісектриса $\angle D_2D_0D_3$, а $D_0B$ – бісектриса зовнішнього кута, отже $\frac{D_1D_2}{D_1D_3} = \frac{BD_2}{BD_3}$, що й треба було довести.
</details>

# 4 тур
## 10
Нехай $b$, $n > 1$ – деякі натуральні числа. Припустимо, що для кожного $k > 1$ існує натуральне число $a_k$ таке, що $b-a_k^n$ ділиться на $k$. Доведіть, що $n = A^n$ для деякого натурального числа $A$.
<details><summary>Розв’язання</summary>

Розглянемо розклад числа $b$ на прості множники: $b = p_1^{\alpha_1}\cdots p_s^{\alpha_s}$, де $p_1$, $\cdots$, $p_s$ – різні прості числа. Доведемо, що всі показники $\alpha_i$ діляться на $n$, тоді можна буде покласти $A = p_1^\frac{\alpha_1}{n}\cdots p_s^\frac{\alpha_s}{n}$.

Застосуємо умову до $k = b^2$. Число $b - a_k^n$ ділиться на $b^2$ за умовою, а тому для кожного $1 \le i \le s$, воно також ділиться на $p_i^{2\alpha_i} > p_i^{\alpha_i}$. Тому $a_k^n \equiv b \equiv 0 \mod p_i^{\alpha_i}$ та $a_k^n \equiv b \not\equiv 0 \mod p_i^{\alpha_i + 1}$, що доводить, що степінь $p_i$ в розкладі $a_k^n$ є $p_i^{\alpha_i}$. А так як $a_k^n$ - це повна $n$-та степінь, то $n\mid \alpha_i$.
</details>

## 11
Про опуклий п’ятикутник $A_1A_2A_3A_4A_5$ відомо, що рівні площі п’яти таких трикутників: $S_{A_1A_2A_3} = S_{A_2A_3A_4} = S_{A_3A_4A_5} = S_{A_4A_5A_1} = S_{A_5A_1A_2}$. Довести, що існує така точка $M$, що рівні площі п’яти таких трикутників: $S_{A_1A_2M} = S_{A_2A_3M} = S_{A_3A_4M} = S_{A_4A_5M} = S_{A_5A_1M}$.
<details><summary>Розв’язання</summary>

З умови рівності площ $S_{A_1A_2A_3} = S_{A_2A_3A_4} =S_{A_3A_4A_5} = S_{A_4A_5A_1} = S_{A_5A_1A_2}$ випливає, що для цього необхідно й достатньо, щоб сторони п’ятикутника були паралельними відповідним протилежним діагоналям, тобто $A_1A_2 \parallel A_5A_3,\ldots,A_5A_1 \parallel A_4A_2$. Це відразу можна одержати, якщо розглянути сусідні трикутники, як трикутники із спільною основою. Позначимо точки перетину діагоналей п’ятикутника. У нас утворилося 5 паралелограмів, як чотирикутників з паралельними протилежними сторонами – $A_1A_2C_1A_5,\ldots,A_5A_1C_5A_4$. Тому $A_1A_2 = A_5C_1 = C_2A_3,\ldots,A_5A_1 = A_4C_5 = C_1A_2 \implies A_1C_4 = A_3C_5,\ldots,A_1C_3 = A_4C_2$.

З паралельності маємо такі пари подібних трикутників: $\triangle A_5C_3C_2 \sim \triangle A_3C_2A_4,\ldots,\triangle A_4C_2C_1 \sim \triangle A_2C_1A_3$, а також $\triangle A_1A_5C_3 \sim \triangle A_2A_4C_3 = \triangle A_2A_4A_3,\ldots,\triangle A_5A_4C_2 \sim \triangle A_1A_3C_2 = \triangle A_1A_3A_2$ тому з одержаних подібностей можемо записати такі рівності: $\frac{A_1A_2}{A_2A_3} = \frac{A_5C_2}{C_2A_4} = \frac{C_2A_3}{C_3A_4}$ (кожна з таких рівностей має 5 аналогічних), $\frac{C_3C_2}{C_2A_4} = \frac{C_2A_5}{C_2A_3} = \frac{C_2A_4}{C_3A_4}$, що випливає з попередньої рівності. Тому $\frac{C_3C_2}{C_2A_4} = \frac{C_2A_4}{C_2C_3 + C_2A_4} \implies \frac{C_3C_2}{C_2A_4} \cdot \left( \frac{C_3C_2}{C_2A_4} + 1 \right) = 1 \implies \frac{C_3C_2}{C_2A_4} = \frac{-1 + \sqrt{5}}{2}$. $\frac{A_1 A_4}{A_2 A_3} = \frac{A_1 C_3 + C_3 A_4}{C_3 A_4} = 1 + \frac{A_4 C_2}{A_4 C_2 + C_2 C_3} = 1 + \frac{1}{1 + \frac{C_2 C_3}{C_2 A_4}} = \frac{\sqrt{5} + 1}{2}$, зрозуміло, що п’ять аналогічних пар відрізків мають таке саме відношення. Тому $\triangle C_1 C_2 C_3 \sim \triangle A_3 C_2 A_1$, звідки $C_1 C_3 \parallel A_1 A_3$.

Позначимо через $B_1$, $\ldots$, $B_5$ – середини відповідних діагоналей п’ятикутника, і точки перетину таких прямих: $A_4 B_4 \cap A_3 B_3 = T$, $A_4 B_4 \cap A_5 B_5 = K$. Оскільки $B_4$ та $B_5$ – середини відрізків $C_1 C_2$ та $C_2 C_3$ відповідно, то $B_4 B_5 \parallel C_1 C_3 \parallel A_1 A_3 \parallel A_4 A_5$, тому $\triangle KB_4 B_5 \sim \triangle KA_4 A_5 \implies \frac{KB_4}{KA_4} = \frac{B_4 B_5}{A_4 A_5} = \frac{\frac{1}{2}C_1 C_3}{A_4 A_5}$, оскільки $\frac{C_1 C_3}{A_4 A_5} = \frac{A_2 C_1}{A_2 A_4} = \frac{A_1 A_5}{A_2 A_4} = \frac{\sqrt{5} - 1}{2}$, отже $\frac{KB_4}{KA_4} = \frac{\sqrt{5}-1}{4}$, повністю аналогічно одержимо, що $\frac{TB_4}{TA_4} = \frac{\sqrt{5}-1}{4}$, тобто точки $K$ і $T$ співпадають. Звідси випливає, що прямі $A_iB_i$, $i=\overline{1,5}$ перетинаються в одній точці. Позначимо її $M$ та доведемо, що вона шуканна.

Нехай $A_4U$ та $A_2V$ – висоти трикутників $A_2A_3M$ та $A_4A_3M$. Маємо за побудовою точки $B_3$ такі рівності $A_2V = A_2B_3 \cdot \sin \angle A_2B_3A_3 = A_4B_3 \cdot \sin \angle A_4B_3A_3= A_4U$, звідки $S_{MA_2A_3} = S_{MA_3A_4}$, повністю аналогічно для інших трикутників, звідки маємо шукану рівність для точки $M$.
</details>

## 12
Довести, що для будь-яких натуральних $m$, $n$ многочлен $\sum_{i=0}^{m} C_{n+i}^n x^i$ має не більше одного дійсного кореня.
<details><summary>Розв’язання</summary>

Будемо доводити твердження індукцією за змінною $m$. База для $m = 1$ є очевидною, оскільки степінь многочлена дорівнює 1. Нехай ми вже довели наше твердження для усіх $k \leq m$ (тобто той факт, що для $k \leq m$ та довільного $n$ наш многочлен має не більше одного дійсного кореня). Доведемо тоді його для $k = m + 1$. Для цього помітимо, що справджується наступне:
1. $P_{n,m}'(x) = (n + 1)P_{n+1,m-1}(x)$;
2. $P_{n,m}(x) = \frac{1}{n+1}\left((1 - x)P_{n,m}'(x)\right) + C^{m}_{n+m+1}x^{m}$.

Тепер розглянемо декілька випадків.
- $m$ – парне. Тоді, якщо для якогось $n$ многочлен $P_{n,m+1}(x)$ мав би більше одного дійсного кореня, то його похідна $P_{n,m+1}'(x)$ мала би принаймні один дійсний корінь, отже внаслідок (1) принаймні один дійсний корінь мав би і многочлен $P_{n+1,m}(x)$. Але многочлен $P_{n+1,m}(x)$ має парний степінь, отже він має ще один дійсний корінь, відмінний від першого, і ми приходимо до протиріччя з припущенням індукції. Те, що у наших многочленів немає кратних коренів випливає з (2).
- $m$ – непарне. Припустимо, що існує натуральне $n$, для якого многочлен $P_{n,m+1}(x)$ має більше одного дійсного кореня. Позначимо через $x_1 < x_2$ деякі два з його коренів. Тоді за теоремою Ролля існує $y \in (x_1, x_2)$, для якого $P_{n,m+1}'(y) = 0$. Помітимо далі, що многочлен $P_{n+1,m}(x)$, а отже з (1) і $P_{n,m+1}'(x)$ є зростаючою функцією. Дійсно, внаслідок (2) $P_{n+1,m}'(x) = (n + 2)P_{n+2,m-1}(x)$, а многочлен $P_{n+2,m-1}(x)$ має за припущенням індукції не більше одного дійсного кореня і кратних коренів немає, що означає, що він не має жодного дійсного кореня. А тоді дійсних коренів не має і $P_{n+1,m}'(x)$, і отже $P_{n+1,m}(x)$ таки є зростаючою функцією. З цього випливає, що $P_{n,m+1}'(x_2) > P_{n,m+1}'(y) = 0$. Але тоді внаслідок (2) ми маємо, що $P_{n,m+1}(x_2) = \frac{1}{n+1}\left((1 - x_2)P_{n,m+1}'(x_2)\right) + C^{m+1}_{n+m+2}x^{m+1} > 0$, бо $x_2$, очевидно, має бути від'ємним, і ми знов приходимо до протиріччя.
</details>

# [XLIX Міжнародна математична олімпіада](http://imo-official.org/team_r.aspx?code=UKR&year=2008)
## 🥇
|Ім'я|Навчальний заклад|
|---|---|
|Міщенко Павло Андрійович|Донецький загальноосвітній спеціалізований санаторний інтернатний заклад II-III ступенів "Ерудит" для обдарованих дітей|
|Шишацький Юрій Олександрович|Києво-Печерський ліцей №171 "Лідер" м. Києва|
## 🥈
|Ім'я|Навчальний заклад|
|---|---|
|Сердюк Назар Павлович|Ліцей №208 Дніпровського району|
|Соболєв Дмитро Якович|Харківська гімназія №47|
## 🥉
|Ім'я|Навчальний заклад|
|---|---|
|Сенін Віталій Ігорович|Ліцей №208 Дніпровського району|
|Семікіна Юлія Сергіївна|Києво-Печерський ліцей «Лідер» №171 Печерського району|
