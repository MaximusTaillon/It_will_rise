import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ArrowDown, Droplets, ThermometerSun, Wind } from "lucide-react";
import { Card } from "@/components/ui/card";

const Index = () => {
  const [scrolled, setScrolled] = useState(false);
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setCounter((prev) => (prev < 3.3 ? prev + 0.1 : prev));
    }, 100);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-b from-sky-50 to-sky-100">
      {/* Hero Section */}
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
             <h1 className="text-4xl md:text-6xl font-bold text-white"> un problème majeur
            </h1>
            <br> 
            </br>
            <p className="text-lg md:text-xl text-gray-200 mb-8 max-w-2xl mx-auto">
             Voyez l'effet de l'augmentation du niveau de la mer sur les villes de Shangai, Bangkok et Amsterdam
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

      {/* Stats Section */}
      <section className="py-20 bg-white/50 backdrop-blur-sm">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              viewport={{ once: true }}
              className="stat-card"
            >
              <Droplets className="w-12 h-12 text-primary mb-4" />
              <h3 className="text-4xl font-bold mb-2">{counter.toFixed(1)}mm</h3>
              <p className="text-gray-600">Augmentation annuelle du niveau de la mer</p>
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
              <p className="text-gray-600">Global Temperature Rise</p>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.4 }}
              viewport={{ once: true }}
              className="stat-card"
            >
              <Wind className="w-12 h-12 text-primary mb-4" />
              <h3 className="text-4xl font-bold mb-2">680M</h3>
              <p className="text-gray-600">People at Coastal Risk</p>
            </motion.div>
          </div>
        </div>
      </section>
      
 {/* Section simulation */}
      <section className="py-20 backdrop-blur-sm">
        <div className="container mx-auto px-4">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="text-4xl font-bold text-center mb-16"
          >
            Simulation du niveau de la mer 
          </motion.h2>
          <script>
            
          </script>
        </div>
      </section>

        
      {/* Impact Cards */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="text-4xl font-bold text-center mb-16"
          >
            Understanding the Impact
          </motion.h2>
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

      {/* Call to Action */}
      <section className="py-20 bg-primary text-white">
        <div className="container mx-auto px-4 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="max-w-2xl mx-auto"
          >
            <h2 className="text-4xl font-bold mb-6">Take Action Today</h2>
            <p className="text-lg mb-8">
              Learn more about how you can help protect our coastlines and communities.
            </p>
            <button className="px-8 py-3 bg-white text-primary rounded-lg font-semibold hover:bg-opacity-90 transition-colors duration-300">
              Learn More
            </button>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

const impacts = [
  {
    title: "Coastal Communities",
    description:
      "Rising seas threaten to displace millions of people living in coastal areas, affecting homes, infrastructure, and livelihoods.",
  },
  {
    title: "Ecosystems",
    description:
      "Coastal ecosystems face unprecedented challenges as rising waters alter habitats and threaten biodiversity.",
  },
  {
    title: "Infrastructure",
    description:
      "Critical infrastructure like ports, roads, and power plants face increased risks from flooding and storm surges.",
  },
  {
    title: "Economy",
    description:
      "The global economy faces significant challenges as coastal cities adapt to rising seas and extreme weather events.",
  },
];

export default Index;
