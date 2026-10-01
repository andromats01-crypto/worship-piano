import pathlib
m='<?xml version="1.0" encoding="utf-8"?><manifest xmlns:android="http://schemas.android.com/apk/res/android"><application android:label="Alvin Piano" android:theme="@android:style/Theme.NoTitleBar"><activity android:name=".MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity></application></manifest>'
open('app/src/main/AndroidManifest.xml','w').write(m)
s='<resources><string name="app_name">Alvin Piano</string><string-array name="instruments"><item>Piano</item><item>Strings</item><item>Pad</item><item>Choir</item><item>Bass</item></string-array></resources>'
open('app/src/main/res/values/strings.xml','w').write(s)
l='''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent" android:background="#0F172A" android:padding="10dp">
<TextView android:layout_width="match_parent" android:layout_height="wrap_content" android:text="ALVIN PIANO - 5 LAYER REAL" android:textColor="#FFD700" android:gravity="center" android:textStyle="bold" android:padding="8dp"/>
<Spinner android:id="@+id/spin1" android:layout_width="match_parent" android:layout_height="40dp" android:background="#1E293B"/>
<SeekBar android:id="@+id/vol1" android:layout_width="match_parent" android:layout_height="wrap_content" android:max="100" android:progress="100"/>
<Spinner android:id="@+id/spin2" android:layout_width="match_parent" android:layout_height="40dp" android:background="#1E293B"/>
<SeekBar android:id="@+id/vol2" android:layout_width="match_parent" android:layout_height="wrap_content" android:max="100" android:progress="80"/>
<Spinner android:id="@+id/spin3" android:layout_width="match_parent" android:layout_height="40dp" android:background="#1E293B"/>
<SeekBar android:id="@+id/vol3" android:layout_width="match_parent" android:layout_height="wrap_content" android:max="100" android:progress="70"/>
<Spinner android:id="@+id/spin4" android:layout_width="match_parent" android:layout_height="40dp" android:background="#1E293B"/>
<SeekBar android:id="@+id/vol4" android:layout_width="match_parent" android:layout_height="wrap_content" android:max="100" android:progress="60"/>
<Spinner android:id="@+id/spin5" android:layout_width="match_parent" android:layout_height="40dp" android:background="#1E293B"/>
<SeekBar android:id="@+id/vol5" android:layout_width="match_parent" android:layout_height="wrap_content" android:max="100" android:progress="50"/>
<LinearLayout android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="80dp"><Button android:id="@+id/btn_c" android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:text="C"/><Button android:id="@+id/btn_d" android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:text="D"/><Button android:id="@+id/btn_e" android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:text="E"/><Button android:id="@+id/btn_f" android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:text="F"/><Button android:id="@+id/btn_g" android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:text="G"/></LinearLayout></LinearLayout>'''
open('app/src/main/res/layout/activity_main.xml','w').write(l)
j='''package com.alvin.piano;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import androidx.appcompat.app.AppCompatActivity;
import org.billthefarmer.mididriver.MidiDriver;
public class MainActivity extends AppCompatActivity implements MidiDriver.OnMidiStartListener{
private MidiDriver midi;
private int[] vols={100,80,70,60,50};
@Override protected void onCreate(Bundle b){
super.onCreate(b);
setContentView(R.layout.activity_main);
midi=MidiDriver.getInstance();
midi.setOnMidiStartListener(this);
Spinner[] sp=new Spinner[5];
sp[0]=findViewById(R.id.spin1);sp[1]=findViewById(R.id.spin2);sp[2]=findViewById(R.id.spin3);sp[3]=findViewById(R.id.spin4);sp[4]=findViewById(R.id.spin5);
ArrayAdapter ad=ArrayAdapter.createFromResource(this,R.array.instruments,android.R.layout.simple_spinner_item);
ad.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
for(int i=0;i<5;i++)sp[i].setAdapter(ad);
findViewById(R.id.btn_c).setOnClickListener(v->play(60));
findViewById(R.id.btn_d).setOnClickListener(v->play(62));
findViewById(R.id.btn_e).setOnClickListener(v->play(64));
findViewById(R.id.btn_f).setOnClickListener(v->play(65));
findViewById(R.id.btn_g).setOnClickListener(v->play(67));
}
void play(int note){for(int ly=0;ly<5;ly++){if(vols[ly]==0)continue;byte[] pc=new byte[]{(byte)(0xC0+ly),(byte)(ly*8)};midi.write(pc);byte[] on=new byte[]{(byte)(0x90+ly),(byte)note,(byte)vols[ly]};midi.write(on);byte[] off=new byte[]{(byte)(0x80+ly),(byte)note,(byte)0};midi.getHandler().postDelayed(()->midi.write(off),800);}}
public void onMidiStart(){}
protected void onResume(){super.onResume();midi.start();}
protected void onPause(){super.onPause();midi.stop();}
}'''
open('app/src/main/java/com/alvin/piano/MainActivity.java','w').write(j)
print('5-Layer files created OK')
