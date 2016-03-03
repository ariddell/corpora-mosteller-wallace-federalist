function [train,tune,test,dataDim] = getFederalistData
% syntax: [train,tune,test,dataDim] = getdata
% extract data from the database file federalData.mat

load federalData
dataDim = size(data,2) - 1;
labels = data(:,1);
test = data(find(labels==3),2:end);
train = data(find(labels~=3),:);
tune = train(1:20,:);
train = train(21:end,:);
return;
