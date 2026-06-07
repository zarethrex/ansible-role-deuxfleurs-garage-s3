vagrant_dir = File.dirname(__FILE__)

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-25.04"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.disk :disk, size: "20GB", primary: true

  config.vm.network "private_network", ip: "192.168.56.4"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.limit = "all"
    ansible.playbook = File.join(vagrant_dir, "tests", "playbook.yml")
    ansible.extra_vars = {
      "garage_install_rpc_secret": "ffad5bfcd8ce69fe30ba3a7493147ff67eb2b9bb508782c6426d5900a9a5a72c"
    }
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
  end
end
