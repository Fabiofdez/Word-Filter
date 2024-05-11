# Word Filter

Word Filter is a simple utility that provides a list of words that contain a specified substring 
and sample paragraphs with those words in context.

## Features

The script takes a text corpus in the format of text corpora provided by the Leipzig Corpora Collection. 
Specifically, the files expected are a directory containing files with similar names, with words 
and sentences to parse. The words file is a list of tab-separated frequency, word pairs with one word 
per line, sorted first in descrnding order of frequency, then in alphabetical order. The sentences 
file contains one sentence per line. If no files are specified, a dfault.txt file could be defined with 
a list of sentences to be parsed and used instead.

Word Filter will provide 2 lists of words, the first being the most frequently-occurring words containing
the given substring, and the second a randomly selected list of such words. If the --print-sample (-p) flag 
is specified, there will also be corresponding paragraphs compiled from sentences containing the words in the
afrementioned lists, though if a word is nt found in the sentence files it will not appear in the paragraphs.
The paragraphs mainly serve to provide an artificial context for the words, though the sentences may and in 
all likelyhood will be on completely unrelated subjects (hence artificial context).

To get started, clone this repository and make sure to have python3 and/or a python environment active.
to run the script, use the command:

```python word-filter.py [arguments]```

### The following arguments are accepted:

- `-f, --files`: The directory of corpus files (.txt) located in a ```data``` folder in the same directory as the script.
- `-s, --substring`: (required) The substring words should contain.
- `-c, --count`: The number of words to find.
- `-p, --print-sample`: (flag, false by default) Whether to provide a paragraph with the found words in an artificial context.

An example use is as follows, specifying 5-length lists of words containing the substring "lf", 
along with corresponding sample paragraphs, from parsing the "data/default.txt" file:

```python word-filter.py -s lf -c 5 -p```

and the output could be as follows (in this case, default corpus data is from external source, not Leipzig Corpora Collection):

```
Top 5 most frequent words with "lf":
 > alfombras
 > alfil
 > delfines
 > analfabetismo
 > alfombra

Random selection of 5 words with "lf":
 > diazobenzolsulfónico
 > woolf
 > mbtlfno
 > alfombrado
 > alfileres


Corpus 1 (most-frequent):

Sólo falta ver alfombras voladoras y uno se creería metido en uno de los cuentos de las Mil y Una Noches.
 Ta Aa Las blancas sacrifican en el flanco de dama para operar cómodamente en el de rey pues su alfil de
casillas negras y el caballo podrán tras la desviación de piezas demostrar la superioridad en el sector.
Tyra Banks no puede ver a los delfines. Como Ministerio llevamos adelante el Plan Nacional de Alistamiento
Digital para empoderar a la población ecuatoriana en el manejo perfeccionamiento y buen uso de las TIC con
el objeto de erradicar el analfabetismo digital y promover una escolarización de calidad. Si tu sala lo
decoraste con colores neutros o claros te aconsejo que en el piso coloques una hermosa alfombra que tenga
colores brillantes y que contenga formas geométricas. 


Corpus 2 (random):

Reacción de Ehrlich Racción observada en la orina de algunos enfermos febriles especialmente en la fiebre
tifoidea que consiste en la aparición de un color rojo por la adición de ácido diazobenzolsulfónico y
amoníaco ácido que se forma haciendo actuar sobre una solución acidulada de ácido sulfanílico una solución
de nitrito de sodio a el. Estas fueron algunas de las palabras plasmadas en la carta con la que Virginia
Woolf se despidió de su marido Leonard Woolf. IZhola ayer llame a ONO porque me dijeron que amenazando con
dar te de baja te daban la oferta de MB de cliente nuevo yo tengo MBtlfno. Esta alfombrado hasta el
maletero bueno les aseguro como les decía que esta ok yo soy músico y lo arregle para mí nunca lo cojo
para botear. Sentí como si millones de pequeños alfileres se clavasen en mi cuerpo.
```

Text corpora data provided by: 

D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012
