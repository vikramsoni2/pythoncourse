---
title: Fundamental of Computer
---

**Fundamentals of computer**
============================
 
## What is computer?

A computer is an electronic device that manipulates information, or data. It has the ability to store, retrieve, and process data. It can process information in very fast speed. You can use a computer to type documents, send email play games, and browse the Web. You can also use it to edit or create spreadsheets, presentations, and even videos

---

## Hardware
Hardware is any part of computer that has physical structure. Such as keyboard, mouse, processor, hard disk, or any other component. Hardware is used for getting input from user, processing and giving output to user.

Hardware are further categorized into several categories:  

**Input Devices** - Any device which is used to get input from user such as keyboard, mouse, scanner etc.  
  
**Output Devices** - Any device which provides output to user such as monitor, printer. 

**Storage Devices** - storage devices are used to store information. such as hard disk, Usb drive etc.


A modern computer is like a Lego, all components can be attached detached very easily.  

<img width="300" src="https://blog.se.com/wp-content/uploads/2013/12/Building-Blocks-with-Legos.jpg"/>

### **_Mother Board_**
<img width="300" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Intel_D945GCCR_Socket_775.png/1920px-Intel_D945GCCR_Socket_775.png"/>

The motherboard is the computer's main circuit board. It's a thin plate that holds the CPU, memory, connectors for the hard drive and optical drives, expansion cards to control the video and audio, and connections to your computer's ports (such as USB ports). The motherboard connects directly or indirectly to every part of the computer.

### **_Hard Disk_**
<img width="300" src="https://sites.google.com/site/iebitwiki/_/rsrc/1343238980021/hardware/secondary-storage/hard-disk-drive/hdd.jpg"/>

It is a magnetic storage device, made of multiple flat circular disks stacked on top of each other. The disks are made of glass and coated with magnetic material. Hard disks can store large amount of data.

It has a head ( just like the old music disk player ) which can read and write information to the disk. 

The data in hard disk are stored in binary format ( 0 or 1 ). In order to write data on to disk, the head magnetize a tiny spot on the disk for writing 1 and demagnetize for writing 0. 

And later when reading it can retrive the information by finding the magnetized/demagnetized spots.

### **_SSD_**
<img width="300" src="https://image-us.samsung.com/SamsungUS/home/computing/memory-and-storage/solid-state-drives/pdp/mz-v7e500bw/gallery-v2/001_gallery_MZ-V7E500BW_09-28-18.jpg?$product-details-jpg"/>

A solid-state drive (SSD) is a new generation of storage device used in computers. SSDs replace traditional mechanical hard disks by using flash-based memory, which is significantly faster. Older hard-disk storage technologies run slower, which often makes your computer run slower than it should. SSDs speed up computers significantly due to their low read-access times and fast throughputs.



### **_RAM ( Random Access Memory )_**
<img width="300" src="https://www.vsgamers.es/thumbnails/product_gallery_medium/uploads/products/kingston/memoria-ram/memoria-ddr4-8gb-kingston/kingston-technology-valueram-ddr4-8gb-3200-mhz-cl22-galeria.jpg"/>

RAM is essentially your device’s short-term memory. It temporarily stores (remembers) everything that runs on your PC, like your web browser, your opened applications or the game you’re playing. Any program you load on your computer is first transferred from Hard Disk to RAM. 

Data that resides in the short-term memory, or RAM, can be read from anywhere at almost the same speed. Because it has a hard-wired connection to your system, there’s no real latency in cabling or connection.

RAM doesn’t remember everything forever, however. It’s a “volatile” technology, meaning that once it loses power, it forgets everything. That makes it perfect for handling the multitude of high-speed tasks that your system throws at it on a daily basis. But it’s also why we need storage systems like hard drives and SSDs, which actually hold our information when you turn the system off.


### **_Processor ( CPU )_**
<img width="300" src="https://images.idgesg.net/images/article/2018/02/install-intel-cpu-motherboard-100748992-large.jpg"/>

The central processing unit (CPU), also called a processor, is located inside the computer case on the motherboard. It is sometimes called the brain of the computer, and its job is to carry out commands. Whenever you press a key, click the mouse, or start an application, you're sending instructions to the CPU.  
  
  
---

## Software
Software, also known as application or a computer program – is a collection of many lines of code.  
A smallest program can have hundreds of lines of codes in them. A large application can have billions of lines.

We call it code because it is a language which is understandable by computer. They are step by step instructions. Like a recipe which tells computers what to do with the data. 

Data is a pirce of information that the computer can hold in its memory. Computer takes information from user through input devices and provides it to program which tells processor what to do with the data. And once the processor finish processing the data, the program collects the output and presents it to the user.

### **_Operating System_**

An operating system is the most important software that runs on a computer. It manages the computer's memory and processes, as well as all of its software and hardware. It also allows you to communicate with the computer without knowing how to speak the computer's language. Without an operating system, a computer is useless.

An operating system takes many roles to manage the computer:  

**As a resource manager** - Operating system's job invludes managing resources like hard disk, ram etc when multiple tasks are running. 

It also prioritize which application should be executed first by the processor. Also when you save any document on microsoft word. Its the operating system which takes care of storing the information to the disk. 

**As an interface for programs** - It also provices an interface for other programs to run. When you write program in python, you just need to install python interpretor for your operating system. 

Any code you write in python is processed by the interpretor. The interpretor communicates with the operating system and the operating system runs the task on processor.

![](https://upload.wikimedia.org/wikipedia/commons/c/c6/Layers_in_computer_systems.jpg)



----

We can dive deeper into how the operating system works and other things like networks, wired, wifi etc. But for now lets start with some simple programming to get practicing. And we will touch these topics later as we progress.


## Tools for programming

The hardware of a computer understands a low-level instruction set. The numeric codes for the instruction set are called machine code. 

In order to be able to run your own program, you need a tool called compiler / interpreter. They are available for different operating systems. So if you have compiler for Linux, you can run your program on Linux using that compiler. And the same program can be run without any changes to Windows if we have the compiler for windows for that programming language. 

**Compiler** - A compiler is a tool which is used to converts the text of a programming language (called source code) into machine code. The machine code can then be executed on the machine, without the original source code being present. Examples of compiled programming languages are C and C++.

<img width="300" src="https://miro.medium.com/max/692/1*jtuu7CroVW2UTygRXHSXPQ.png"/>

**Interpreter** - An interpreter is a tool which takes the source code of a program and executes it immediately. The operations of the language are provided by the machine code of the interpreter, but how they are composed into a larger program is determined by the source code. Examples of interpreted languages are Perl, Python and Matlab.
<br/><br/>

Apart from translating and running our program in the machine, compiler / interpreter also does the job of analyzing our code and providing us with meaningful error if there is some mistake in our code.

Interpreters and compilers are very similar in structure. The main difference is that an interpreter directly executes the instructions in the source programming language while a compiler translates those instructions into efficient machine code.

---
## Programming languages

Computers are very dumb at understanding instructions, Thats why we need to write the instructions in a special language called **Programming Language** so that it can be understood by computer.

A programming language is nothing but set of tools available for us to write instructions for our program. Some examples of programming language are _java_, _visual Basic_, _python_, _C++_, _Javascript_ etc.

Every programming language has its own style of writing the code, thats called **Syntax**. The below image shows example of how Java and Python have different syntax for the **exact same  program.**

### **_Java vs Python :_**  
<img width="800" src="https://raw.githubusercontent.com/vikramsoni2/pythoncourse/master/java_vs_python.png"/>

Clearly there are different way to write the same function in both languages. We will look deeper in next chapter about building blocks of a program.


---

## Why Python ?

For our introduction to programming we are going to use Python as our programming language. The reason is because python is very versatile, it can be used for all kind of programming, and its syntax makes it simple and less lines of code to write. 

* Its easy to learn and use
* Mature and has big active community
* Libraries and Frameworks are available for everything
* Cross platform, versatile and fast
* Big Data, Machine Learning and Cloud Computing
* Automation


## Installing python

To begin writing our program in python, first we need to download and install python interpreter on our computer. We are going to use anaconda software for pythong. Anaconda is a package which installs python along with most of the commly used tools which we will need to use in python later.  

Please download the anaconda from below link for windows 10:  
https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe

For instructions on how to install anaconda, follow this link:  
https://docs.anaconda.com/anaconda/install/windows/


Once the anaconda is installed, please follow the below steps to verify that the python is available.

1. Click on Start Menu
2. After the start menu opens, type 'CMD', you will see "Command Prompt" in the result. click on it.  
   <img width="500" src="https://raw.githubusercontent.com/vikramsoni2/pythoncourse/master/start.png"/>

3. This will open a command window. In this window, please type `python --version` and hit Enter.  
<img width="600" src="https://raw.githubusercontent.com/vikramsoni2/pythoncourse/master/cmd.png"/>  
This should display the python version which is installed on your computer. The version could be different than what appears in the picture. If you see the version, it means that the python has been setup correctly.
    
---
## Your first program in python

once the python has been setup correctly, we can start writing our first program. **Lets try using python as a calculator**

1. Open the command prompt again as described in the previous step. Or you can use the same window if you already have it opened. 
2. Type `python` and hit Enter. This should display a line with >>> something like this:  
<img width="800" src="https://raw.githubusercontent.com/vikramsoni2/pythoncourse/master/python.png"/>\

Once you are presented with `>>>` prompt, try doing some maths like `2+2` or `2**6` or ` 10 + 20 + 30 + 40` etc. after every operation you can hit Enter and you will see the result presented in the below line. 



## Building blocks of a program

To undrestand a typical program we need to go through the following building blocks of a program:

* Syntax
* Kaywords and Idenfitiers
* Statements
* Datatypes
* Operators
* Variables
* Import and I/O
* Python indentation



### Keywords

Keywords are reserved words in programming language which has its own special meaning. You cannot create a function or a variable with the name same as keywords.

<img width="600" src="https://raw.githubusercontent.com/vikramsoni2/pythoncourse/master/python-keywords.png"/>


---
## Next Steps
```
    - how the program works on computer ( interpreter, compiler )
    - mental strategy 
    - structure of program
    - tools for programming ( python ) 




    * parts of program 
        - data types
        - values and expression
        - control structure  ( if/else, conditions)
        - iterations ( for, while )
        - functions ( grouping instructions together)

    * software development lifecycle
        - plan
        - development
        - testing
        - deployment ( launch ) final product

```
```mermaid
graph LR;
Input-->Processing;
subgraph  
Processing-->Storage;
Storage-->Processing;
end
Processing-->Output;
```


