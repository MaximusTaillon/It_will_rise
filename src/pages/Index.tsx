
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ArrowDown, Droplets, ThermometerSun, Snowflake } from "lucide-react";
import { Card } from "@/components/ui/card";
import { Slider } from "@/components/ui/slider";

const Index = () => {
  const [scrolled, setScrolled] = useState(false);
  const [counter, setCounter] = useState(0);
  const [annee, setAnnee] = useState([2025]);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setCounter((prev) => (prev < 15 ? prev + 0.5 : prev));
    }, 100);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-b from-sky-50 to-sky-100">
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-[url('/floods.jpg')] bg-cover bg-center bg-no-repeat before:absolute before:inset-0 before:bg-black/40">
        <div className="container mx-auto px-4 z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 3 }}
            className="text-center"
          >
            <h1 className="text-5xl md:text-7xl font-bold mb-6 text-white">
              La montée des eaux,
            </h1>
            <h1 className="text-4xl md:text-6xl font-bold text-white">
              un problème majeur
            </h1>
            <br />
            <p className="text-lg md:text-xl text-gray-200 mb-8 max-w-2xl mx-auto">
              Constatez l'effet frappant de l'augmentation du niveau de la mer
            </p>
          </motion.div>
        </div>
        <div className="absolute bottom-0 left-0 right-0 h-64 bg-gradient-to-t from-sky-200/50 to-transparent">
          <div className="wave" style={{ bottom: "20px", opacity: "0.7" }}></div>
          <div className="wave" style={{ bottom: "10px", opacity: "0.5", animationDelay: "-2s" }}></div>
          <div className="wave" style={{ bottom: "0px", opacity: "0.3", animationDelay: "-4s" }}></div>
        </div>
        <motion.div
          animate={{ y: [0, -10, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
          className="absolute bottom-8 left-1/2 transform -translate-x-1/2 cursor-pointer"
        >
          <ArrowDown className="w-6 h-6 text-white" />
        </motion.div>
      </section>

      <section className="py-20 bg-white/50 backdrop-blur-sm">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl font-bold text-center mb-2">3 causes principales</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              viewport={{ once: true }}
              className="stat-card"
            >
              <Droplets className="w-12 h-12 text-primary mb-4" />
              <h3 className="text-4xl font-bold mb-2">{counter.toFixed(1)} cm</h3>
              <p className="text-gray-600">Une augmentation de 15 cm du niveau de la mer causera environ 20% plus d'inondations </p>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.2 }}
              viewport={{ once: true }}
              className="stat-card"
            >
              <ThermometerSun className="w-12 h-12 text-primary mb-4" />
              <h3 className="text-4xl font-bold mb-2">1.5°C</h3>
              <p className="text-gray-600">Réchauffement de la terre depuis 1850 </p>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.4 }}
              viewport={{ once: true }}
              className="stat-card"
            >
              <Snowflake className="w-12 h-12 text-primary mb-4" />
              <h3 className="text-4xl font-bold mb-2">0</h3>
              <p className="text-gray-600">Si on ne change rien, il ne restera pratiquement plus de glaciers en 2075</p>
            </motion.div>
          </div>
          <p className="text-gray-700 text-center text-lg mt-8 max-w-3xl mx-auto">
            Cela entraîne une augmentation moyenne du niveau de la mer de 3,37 mm par année et ce rythme va accélérer dans les prochaines années
          </p>
        </div>
      </section>

      <section className="py-20 bg-[#7FAFF5]">
        <div className="container mx-auto px-4">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="text-4xl font-bold text-center mb-8 text-white"
          >
            Simulation du niveau de la mer 
          </motion.h2>
          
          <div className="max-w-xl mx-auto space-y-4">
            <p className="text-white text-center text-lg">
              Plusieurs facteurs font en sorte que la ville de Bangkok sera parmi les plus touchées.
            </p>

            <div className="w-full max-w-lg mx-auto rounded-lg overflow-hidden shadow-lg">
              <img 
                src="/bangkok-flooding.gif" 
                alt="Bangkok flooding simulation"
                className="w-full h-auto"
              />
            </div>
            
            <div className="space-y-1 font-bold">
              <div className="flex justify-between text-white text-sm">
                <span>Année</span>
                <span>{annee[0]}</span>
              </div>
              <Slider
                defaultValue={[2025]}
                min={2025}
                max={2300}
                step={1}
                value={annee}
                onValueChange={setAnnee}
                className="py-4"
              />
            </div>
          </div>
        </div>
      </section>

      <section className="py-20">
        <div className="container mx-auto px-4">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="text-4xl font-bold text-center mb-16"
          >
            Chaque millimètre est important
          </motion.h2>
          <p className="text-gray-700 text-center text-lg">
            Une augmentation de quelques millimètres ne semble pas très grave, mais les effet à sont bien réels.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {impacts.map((impact, index) => (
              <motion.div
                key={impact.title}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.2 }}
                viewport={{ once: true }}
              >
                <Card className="p-6 h-full hover:shadow-lg transition-shadow duration-300">
                  <h3 className="text-2xl font-bold mb-4">{impact.title}</h3>
                  <p className="text-gray-600">{impact.description}</p>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-20 bg-primary text-white">
        <div className="container mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="max-w-2xl mx-auto text-left"
          >
            <h2 className="text-4xl font-bold mb-6">Références:</h2>
            <p className="text-sm mb-8 text-white/80">
             https://www.ipcc.ch/report/ar6/wg1/figures/summary-for-policymakers/figure-spm-8/ 
             https://www.spf.org/opri/en/newsletter/34_2.html?full=34_2#:~:text=The%20rise%20in%20the%20sea%20level%20and%20the%20climate%20change,impact%20on%20the%20coastal%20area. 
             https://sealevel.globalchange.gov/sea-level-101/future-sea-level/the-basics/#:~:text=All%20of%20the%20scenarios%20had,today%20and%20in%20the%20future. 
             https://climatedata.ca/resource/understanding-shared-socio-economic-pathways-ssps/ 
             https://psl.noaa.gov/data/gridded/data.cobe2.html 
             https://www.kaggle.com/datasets/kkhandekar/global-sea-level-1993-2021/data 
             https://lovable.dev/projects/7ea75af0-27d4-4242-9818-16a9dd516cd3 
             https://ici.radio-canada.ca/nouvelle/1868450/changement-climatique-canada-nord-tundra-ecosysteme
            </p>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

const impacts = [
  {
    title: "Inondations",
    description:
      "Lors des périodes annuelles d’inondations l’eau va se rendre plus loin à l’intérieur des terres à chaque fois.",
  },
  {
    title: "Catastrophes naturelles",
    description:
      "Les ouragans seront plus forts lorsqu'ils toucheront terre.",
  },
];

export default Index;
