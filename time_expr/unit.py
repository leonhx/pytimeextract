#!/usr/bin/env python
# coding:utf-8

import re

from normalizer import TimeNormalizer

class TimePoint:
    def __init__(self):
        self.tunit = [-1, -1, -1, -1, -1, -1]

class TimeUnit:
    def __init__(self, exp_time, n):
        self.Time_Expression = exp_time
        self.Time_Norm = ''
        self._tp = TimePoint()
        self._to_origin = TimePoint()
        self.__normalizer__ = n
        Time_Normalization()
    def __norm_set__(self, regex, idx):
        pattern = re.compile(regex)
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[idx] = int(m.group())
    def norm_setyear(self):
        pattern = re.compile(u'[0-9]{2}(?=年)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[0] = int(m.group())
            if _tp.tunit[0] > 0 and _tp.tunit[0] < 100:
                if _tp.tunit[0] < 30:
                    _tp.tunit[0] += 2000
                else:
                    _tp.tunit[0] += 1900
            return
        self.__norm_set__(u'[0-9]?[0-9]{3}(?=年)', 0)
    def norm_setmonth(self):
        self.__norm_set__(u'((10)|(11)|(12)|([1-9]))(?=月)', 1)
    def norm_setday(self):
        self.__norm_set__(u'((?<!\\d))([0-3][0-9]|[1-9])(?=(日|号))', 2)
    def norm_sethour(self):
        self.__norm_set__(u'(?<!(周|星期))([0-2]?[0-9])(?=(点|时))', 3)

        pattern = re.compile(u'(中午)|(午间)')
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 10:
                _tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)')
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12

        pattern = re.compile(u'晚');
        m = pattern.match(self.Time_Expression);
        if m:
            if _tp.tunit[3] >= 1 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12
            elif _tp.tunit[3] == 12:
                _tp.tunit[3] = 0
    def norm_setminute(self):
        pattern = re.compile(u'([0-5]?[0-9](?=分(?!钟)))|((?<=((?<!小)[点时]))[0-5]?[0-9](?!刻))');
        m = pattern.match(self.Time_Expression)
        if m:
            if m.group():
                _tp.tunit[4] = int(m.group())

        pattern = re.compile(u'(?<=[点时])[1一]刻(?!钟)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 15

        pattern = re.compile(u'(?<=[点时])半')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 30

        pattern = re.compile(u'(?<=[点时])[3三]刻(?!钟)')
        m = pattern.match(self.Time_Expression)
        if m:
            _tp.tunit[4] = 45
    def norm_setsecond(self):
        self.__norm_set__(([0-5]?[0-9](?=秒))|((?<=分)[0-5]?[0-9]), 5)
    def norm_setTotal(self):
        pattern = re.compile(u'(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]')
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split(':')
            _tp.tunit[3] = int(tmp_parser[0])
            _tp.tunit[4] = int(tmp_parser[1])
            _tp.tunit[5] = int(tmp_parser[2])
        else:
            pattern = re.compile(u'(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]')
            m = pattern.match(self.Time_Expression)
            if m:
                tmp_target = m.group()
                tmp_parser = tmp_target.split(':')
                _tp.tunit[3] = int(tmp_parser[0])
                _tp.tunit[4] = int(tmp_parser[1])

        pattern = re.compile(u'(中午)|(午间)')
        m = pattern.match(self.Time_Expression)
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 10:
                _tp.tunit[3] += 12

        pattern = re.compile(u'(下午)|(午后)|(pm)|(PM)')
        m = pattern.match(self.Time_Expression)
        if m:
            if _tp.tunit[3] >= 0 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12

        pattern = re.compile(u'晚')
        m = pattern.match(selfTime_Expression)
        if m:
            if _tp.tunit[3] >= 1 and _tp.tunit[3] <= 11:
                _tp.tunit[3] += 12
            elif _tp.tunit[3] == 12:
                _tp.tunit[3] = 0

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}-((10)|(11)|(12)|([1-9]))-((?<!\\d))([0-3][0-9]|[1-9])');
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('-')
            _tp.tunit[0] = int(tmp_parser[0])
            _tp.tunit[1] = int(tmp_parser[1])
            _tp.tunit[2] = int(tmp_parser[2])

        pattern = re.compile('((10)|(11)|(12)|([1-9]))/((?<!\\d))([0-3][0-9]|[1-9])/[0-9]?[0-9]?[0-9]{2}')
        m = pattern.match(self.Time_Expression)
        if m:
            tmp_target = m.group()
            tmp_parser = tmp_target.split('/')
            _tp.tunit[1] = int(tmp_parser[0])
            _tp.tunit[2] = int(tmp_parser[1])
            _tp.tunit[0] = int(tmp_parser[2])

        pattern = re.compile('[0-9]?[0-9]?[0-9]{2}\\.((10)|(11)|(12)|([1-9]))\\.((?<!\\d))([0-3][0-9]|[1-9])')
        m = pattern.matcher(self.Time_Expression)
        if m:
            tmp_target = match.group()
            tmp_parser = tmp_target.split('.')
            _tp.tunit[0] = int(tmp_parser[0])
            _tp.tunit[1] = int(tmp_parser[1])
            _tp.tunit[2] = int(tmp_parser[2])
    def norm_setBaseRelated(self):
        time_grid = self.__normalizer__.__time_base__.split('-')
        ini = [int(i) for i in time_grid]
        //TODO
        Calendar calendar = Calendar.getInstance();
        calendar.setFirstDayOfWeek(Calendar.MONDAY);
        calendar.set(ini[0], ini[1]-1, ini[2], ini[3], ini[4], ini[5]);
        calendar.getTime();

        boolean[] flag = {false,false,false};//观察时间表达式是否因当前相关时间表达式而改变时间


        String rule="\\d+(?=天[以之]?前)";
        Pattern pattern=Pattern.compile(rule);
        Matcher match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int day = Integer.parseInt(match.group());
            calendar.add(Calendar.DATE, -day);
        }

        rule="\\d+(?=天[以之]?后)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int day = Integer.parseInt(match.group());
            calendar.add(Calendar.DATE, day);
        }

        rule="\\d+(?=(个)?月[以之]?前)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[1] = true;
            int month = Integer.parseInt(match.group());
            calendar.add(Calendar.MONTH, -month);
        }

        rule="\\d+(?=(个)?月[以之]?后)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[1] = true;
            int month = Integer.parseInt(match.group());
            calendar.add(Calendar.MONTH, month);
        }

        rule="\\d+(?=年[以之]?前)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            int year = Integer.parseInt(match.group());
            calendar.add(Calendar.YEAR, -year);
        }

        rule="\\d+(?=年[以之]?后)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            int year = Integer.parseInt(match.group());
            calendar.add(Calendar.YEAR, year);
        }

        String s = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss").format(calendar.getTime());
        String[] time_fin = s.split("-");
        if(flag[0]||flag[1]||flag[2]){
            _tp.tunit[0] = Integer.parseInt(time_fin[0]);
        }
        if(flag[1]||flag[2])
            _tp.tunit[1] = Integer.parseInt(time_fin[1]);
        if(flag[2])
            _tp.tunit[2] = Integer.parseInt(time_fin[2]);
    }
    public void norm_setCurRelated(){
        String [] time_grid=new String[6];
        time_grid=normalizer.getOldTimeBase().split("-");
        int[] ini = new int[6];
        for(int i = 0 ; i < 6; i++)
            ini[i] = Integer.parseInt(time_grid[i]);

        Calendar calendar = Calendar.getInstance();
        calendar.setFirstDayOfWeek(Calendar.MONDAY);
        calendar.set(ini[0], ini[1]-1, ini[2], ini[3], ini[4], ini[5]);
        calendar.getTime();

        boolean[] flag = {false,false,false};//观察时间表达式是否因当前相关时间表达式而改变时间

        String rule="前年";
        Pattern pattern=Pattern.compile(rule);
        Matcher match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            calendar.add(Calendar.YEAR, -2);
        }

        rule="去年";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            calendar.add(Calendar.YEAR, -1);
        }

        rule="今年";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            calendar.add(Calendar.YEAR, 0);
        }

        rule="明年";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            calendar.add(Calendar.YEAR, 1);
        }

        rule="后年";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[0] = true;
            calendar.add(Calendar.YEAR, 2);
        }

        rule="上(个)?月";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[1] = true;
            calendar.add(Calendar.MONTH, -1);

        }

        rule="(本|这个)月";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[1] = true;
            calendar.add(Calendar.MONTH, 0);
        }

        rule="下(个)?月";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[1] = true;
            calendar.add(Calendar.MONTH, 1);
        }

        rule="大前天";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, -3);
        }

        rule="(?<!大)前天";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, -2);
        }

        rule="昨";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, -1);
        }

        rule="今(?!年)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, 0);
        }

        rule="明(?!年)";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, 1);
        }

        rule="(?<!大)后天";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, 2);
        }

        rule="大后天";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            calendar.add(Calendar.DATE, 3);
        }

        rule="(?<=(上上(周|星期)))[1-7]";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int week = Integer.parseInt(match.group());
            if(week == 7)
                week = 1;
            else
                week++;
            calendar.add(Calendar.WEEK_OF_MONTH, -2);
            calendar.set(Calendar.DAY_OF_WEEK, week);
        }

        rule="(?<=((?<!上)上(周|星期)))[1-7]";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int week = Integer.parseInt(match.group());
            if(week == 7)
                week = 1;
            else
                week++;
            calendar.add(Calendar.WEEK_OF_MONTH, -1);
            calendar.set(Calendar.DAY_OF_WEEK, week);
        }

        rule="(?<=((?<!下)下(周|星期)))[1-7]";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int week = Integer.parseInt(match.group());
            if(week == 7)
                week = 1;
            else
                week++;
            calendar.add(Calendar.WEEK_OF_MONTH, 1);
            calendar.set(Calendar.DAY_OF_WEEK, week);
        }

        rule="(?<=(下下(周|星期)))[1-7]";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int week = Integer.parseInt(match.group());
            if(week == 7)
                week = 1;
            else
                week++;
            calendar.add(Calendar.WEEK_OF_MONTH, 2);
            calendar.set(Calendar.DAY_OF_WEEK, week);
        }

        rule="(?<=((?<!(上|下))(周|星期)))[1-7]";
        pattern=Pattern.compile(rule);
        match=pattern.matcher(Time_Expression);
        if(match.find())
        {
            flag[2] = true;
            int week = Integer.parseInt(match.group());
            if(week == 7)
                week = 1;
            else
                week++;
            calendar.add(Calendar.WEEK_OF_MONTH, 0);
            calendar.set(Calendar.DAY_OF_WEEK, week);
        }

        String s = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss").format(calendar.getTime());
        String[] time_fin = s.split("-");
        if(flag[0]||flag[1]||flag[2]){
            _tp.tunit[0] = Integer.parseInt(time_fin[0]);
        }
        if(flag[1]||flag[2])
            _tp.tunit[1] = Integer.parseInt(time_fin[1]);
        if(flag[2])
            _tp.tunit[2] = Integer.parseInt(time_fin[2]);

    }
    public void modifyTimeBase(){
        String [] time_grid=new String[6];
        time_grid=normalizer.getTimeBase().split("-");

        String s = "";
        if(_tp.tunit[0] != -1)
            s += Integer.toString(_tp.tunit[0]);
        else
            s += time_grid[0];
        for(int i = 1; i < 6; i++){
            s += "-";
            if(_tp.tunit[i] != -1)
                s += Integer.toString(_tp.tunit[i]);
            else
                s += time_grid[i];
        }
        normalizer.setTimeBase(s);
    }

    public void Time_Normalization()
    {
        norm_setyear();
        norm_setmonth();
        norm_setday();
        norm_sethour();
        norm_setminute();
        norm_setsecond();
        norm_setTotal();
        norm_setBaseRelated();
        norm_setCurRelated();
        modifyTimeBase();

        _tp_origin.tunit = _tp.tunit.clone();

        String [] time_grid=new String[6];
        time_grid=normalizer.getTimeBase().split("-");

        int tunitpointer=5;
        while (tunitpointer>=0 && _tp.tunit[tunitpointer]<0)
        {
            tunitpointer--;
        }
        for (int i=0;i<tunitpointer;i++)
        {
            if (_tp.tunit[i]<0)
                _tp.tunit[i]=Integer.parseInt(time_grid[i]);
        }
        String[] _result_tmp=new String[6];
        _result_tmp[0]=String.valueOf(_tp.tunit[0]);
        if (_tp.tunit[0]>=10 &&_tp.tunit[0]<100)
        {
            _result_tmp[0]="19"+String.valueOf(_tp.tunit[0]);
        }
        if (_tp.tunit[0]>0 &&_tp.tunit[0]<10)
        {
            _result_tmp[0]="200"+String.valueOf(_tp.tunit[0]);
        }

        for (int i = 1; i < 6; i++) {
            _result_tmp[i] = String.valueOf(_tp.tunit[i]);
        }

        Calendar cale = Calendar.getInstance();         //leverage a calendar object to figure out the final time
        cale.clear();
        if (Integer.parseInt(_result_tmp[0]) != -1) {
            Time_Norm += _result_tmp[0] + "年";
            cale.set(Calendar.YEAR, Integer.valueOf(_result_tmp[0]));
            if (Integer.parseInt(_result_tmp[1]) != -1) {
                Time_Norm += _result_tmp[1] + "月";
                cale.set(Calendar.MONTH, Integer.valueOf(_result_tmp[1]) - 1);
                if (Integer.parseInt(_result_tmp[2]) != -1) {
                    Time_Norm += _result_tmp[2] + "日";
                    cale.set(Calendar.DAY_OF_MONTH, Integer.valueOf(_result_tmp[2]));
                    if (Integer.parseInt(_result_tmp[3]) != -1) {
                        Time_Norm += _result_tmp[3] + "时";
                        cale.set(Calendar.HOUR_OF_DAY, Integer.valueOf(_result_tmp[3]));
                        if (Integer.parseInt(_result_tmp[4]) != -1) {
                            Time_Norm += _result_tmp[4] + "分";
                            cale.set(Calendar.MINUTE, Integer.valueOf(_result_tmp[4]));
                            if (Integer.parseInt(_result_tmp[5]) != -1) {
                                Time_Norm += _result_tmp[5] + "秒";
                                cale.set(Calendar.SECOND, Integer.valueOf(_result_tmp[5]));
                            }
                        }
                    }
                }
            }
        }
        time = cale.getTime();

        time_full = _tp.tunit.clone();
        time_origin = _tp_origin.tunit.clone();
    }

    public String toString(){
        return Time_Expression+" ---> "+ Time_Norm;
    }