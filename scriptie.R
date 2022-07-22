library(dplyr)

# laad de data
data <- read.csv2('FullGPT.csv')


tab <- table(data$fallacy, data$gpt_adjusted2)

tab2 <- as.data.frame.matrix(tab)

# herordenen kolommen
tab2 <- tab2 %>% relocate(c(`circular reasoning`, `false cause`, `false dilemma`, `faulty generalization`, `straw man`), .after = bandwagon)

write.csv2(tab2, file = 'matrix2.csv')

tab3 <- table(data$gpt_adjusted, data$gpt_adjusted2)

write.csv2(tab3, file = 'matrix3.csv')    
