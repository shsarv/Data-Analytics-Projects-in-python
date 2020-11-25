# Gallery
Here you can checkout the visualizations I made when analysing the `Global Terrorism Database`.
For more information on how the plot where made.
For an in depth explanation of how the data is categorized see the [database manual](http://start.umd.edu/gtd/downloads/Codebook.pdf).

#### Assumptions
Certain assumptions were made about the data.

* I only use data from `2007` to `2017`.
* I only consider attacks that are definitely terrorist attacks.
* For attacks with an unknown number of fatalities I assume no one died.

This means that these visuals should be treated as lower bounds on the actual numbers.

## Deaths by type of attack
On the chart below we see timeseries of fatalities split by type of `attack` for the entire ten year period of the data. Note how there is a surge in deaths around and after `2014`.

![image](https://github.com/besiobu/data-science-portfolio/blob/master/global-terrorism/img/deaths_by_attack_over_time.png)

## Number of attacks by weapon
The second plot in the gallery shows the number of attacks by weapon type and region. As can be seen `explosives` a by far the most popular weapon type. Also note that categories `fake weapons`, `biological` and `radiological` have been left out of the plot due to the scarcity of such attacks.

![image](https://github.com/besiobu/data-science-portfolio/blob/master/global-terrorism/img/attacks_by_weapon.png)


## Attack location by group
Lastly, I present you with a map revealing the attack locations of the `five most deadly` terrorist groups. Each dot represents an attack and each attack is colour coded by group.

![image](https://github.com/besiobu/data-science-portfolio/blob/master/global-terrorism/img/group_attack_annotated_blue_sea.png)